import os
import random
import pickle
from datetime import datetime

import numpy as np
from tensorflow.keras.models import load_model

from music21 import instrument, note, stream, chord



SEQUENCE_LENGTH = 100
GENERATE_LENGTH = 500
TEMPERATURE = 0.9
TOP_K = 10



model = load_model("model.keras")

with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

pitchnames = sorted(set(notes))

note_to_int = {n: i for i, n in enumerate(pitchnames)}
int_to_note = {i: n for i, n in enumerate(pitchnames)}



network_input = []

for i in range(len(notes) - SEQUENCE_LENGTH):
    sequence = notes[i:i + SEQUENCE_LENGTH]
    network_input.append([note_to_int[n] for n in sequence])


pattern = list(random.choice(network_input))

prediction_output = []

previous_index = None



for _ in range(GENERATE_LENGTH):

    prediction_input = np.reshape(pattern, (1, len(pattern), 1))
    prediction_input = prediction_input / float(len(pitchnames))

    prediction = model.predict(prediction_input, verbose=0)[0]

    prediction = np.log(prediction + 1e-10) / TEMPERATURE
    prediction = np.exp(prediction)
    prediction = prediction / np.sum(prediction)


    top_indices = np.argsort(prediction)[-TOP_K:]
    top_probs = prediction[top_indices]
    top_probs = top_probs / np.sum(top_probs)

    index = np.random.choice(top_indices, p=top_probs)

    
    if previous_index == index:
        index = np.random.choice(top_indices, p=top_probs)

    previous_index = index

    result = int_to_note[index]
    prediction_output.append(result)

    pattern.append(index)
    pattern = pattern[1:]

print("Music Generated Successfully!")

offset = 0
output_notes = []

for pattern in prediction_output:

    if "." in pattern or pattern.isdigit():

        notes_in_chord = pattern.split(".")

        chord_notes = []

        for current_note in notes_in_chord:

            new_note = note.Note(int(current_note))
            new_note.storedInstrument = instrument.Piano()
            chord_notes.append(new_note)

        new_chord = chord.Chord(chord_notes)
        new_chord.offset = offset
        output_notes.append(new_chord)

    else:

        new_note = note.Note(pattern)
        new_note.offset = offset
        new_note.storedInstrument = instrument.Piano()
        output_notes.append(new_note)

    
    offset += random.choice([0.25, 0.5, 0.75, 1])

midi_stream = stream.Stream(output_notes)


os.makedirs("generated", exist_ok=True)

filename = datetime.now().strftime("generated/song_%Y%m%d_%H%M%S.mid")

midi_stream.write("midi", fp=filename)

print("Saved:", filename)