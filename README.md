 🎵 Music Generator AI

📌 Project Overview

**Music Generator AI** is an AI-based application that generates MIDI music using Python, TensorFlow, and a trained neural network model. The project learns patterns from existing MIDI songs and uses them to generate new musical sequences.

 ✨ Features

* 🎵 AI-based music generation
* 🎹 Generates MIDI files
* 🤖 Uses a trained machine learning model
* 📂 Includes MIDI training data
* 💾 Saves generated songs for later use
* 🐍 Built with Python
* 🌐 Streamlit-based user interface

🛠️ Technologies Used

* **Python**
* **TensorFlow**
* **Streamlit**
* **Music21**
* **NumPy**
* **Pickle**
* **MIDI**

 📁 Project Structure

```text
Music_Generator_AI/
│
├── app.py
├── generate.py
├── train.py
├── model.keras
├── notes.pkl
├── requirements.txt
├── generated/
├── midi_songs/
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/kunaltanwar441-collab/Music-Generator-AI.git
```

2. Open the project folder

```bash
cd Music-Generator-AI
```

3. Create a virtual environment

```bash
python -m venv venv
```

4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

5. Install the required libraries

```bash
pip install -r requirements.txt
```

▶️ How to Run

Start the Streamlit application using:

```bash
streamlit run app.py
```

After running the command, open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

 🎼 How It Works

1. MIDI files are collected as training data.
2. Musical notes are extracted from the MIDI files.
3. The notes are converted into numerical sequences.
4. A neural network model is trained on these sequences.
5. The trained model predicts new musical notes.
6. The generated notes are converted into a MIDI file.
7. The generated music is saved in the `generated/` folder.

📸 Screenshot

Add a screenshot of the Music Generator application here.

```markdown
![Music Generator AI Screenshot](screenshot.png)
```

Place `screenshot.png` in the main project folder.

🔮 Future Improvements

* Improve the quality of generated music
* Add more musical genres
* Add different instruments
* Add audio preview
* Add MP3/WAV export
* Improve the user interface
* Deploy the application online

👨‍💻 Author

**Kunal Tanwar**

 ⭐ Project

This project was developed to explore **Artificial Intelligence, Machine Learning, Python, and music generation**.
