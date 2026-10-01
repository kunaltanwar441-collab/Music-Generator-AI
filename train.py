from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense

import os
from music21 import converter, instrument, note, chord

notes = []

midi_folder = "midi_songs"

for file in os.listdir(midi_folder):

    if file.endswith(".mid"):

        print(f"Reading: {file}")

        try:
            midi = converter.parse(os.path.join(midi_folder, file))

            try:
                parts = instrument.partitionByInstrument(midi)
                notes_to_parse = parts.parts[0].recurse()
            except:
                notes_to_parse = midi.flat.notes

            for element in notes_to_parse:

                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))

                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))

        except Exception as e:
            print(f"❌ Skipping {file}")
            print(e)

print("\nTotal Notes:", len(notes))

import pickle

with open("notes.pkl", "wb") as file:
    pickle.dump(notes, file)

print("Notes saved successfully!")

print("Notes saved successfully!")

# -------------------------------
# Prepare Training Data
# -------------------------------

import numpy as np
from tensorflow.keras.utils import to_categorical

sequence_length = 100

pitchnames = sorted(set(notes))

note_to_int = {}

for number, note_name in enumerate(pitchnames):
    note_to_int[note_name] = number

network_input = []
network_output = []

for i in range(len(notes) - sequence_length):

    sequence_in = notes[i:i + sequence_length]
    sequence_out = notes[i + sequence_length]

    network_input.append([note_to_int[n] for n in sequence_in])

    network_output.append(note_to_int[sequence_out])

n_patterns = len(network_input)

network_input = np.reshape(
    network_input,
    (n_patterns, sequence_length, 1)
)

network_input = network_input / float(len(pitchnames))

network_output = to_categorical(network_output)

print()
print("Training Data Ready")
print("Total Patterns:", n_patterns)
print("Unique Notes:", len(pitchnames))
print("Input Shape:", network_input.shape)
print("Output Shape:", network_output.shape)

# -------------------------------
# Build LSTM Model
# -------------------------------

model = Sequential()

model.add(LSTM(
    256,
    input_shape=(network_input.shape[1], network_input.shape[2]),
    return_sequences=True
))

model.add(Dropout(0.3))

model.add(LSTM(256))

model.add(Dropout(0.3))

model.add(Dense(228, activation="softmax"))

model.compile(
    loss="categorical_crossentropy",
    optimizer="adam"
)

print()
print("AI Model Created Successfully!")
model.summary()


print("\nStarting AI Training...")

history = model.fit(
    network_input,
    network_output,
    epochs=30,
    batch_size=64
)

print("\nTraining Completed Successfully!")


model.save("model.keras")

print("Model saved successfully!")