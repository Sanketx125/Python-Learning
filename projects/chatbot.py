import os
import sys
import pyaudio
import speech_recognition as sr
import sklearn.mixture as mixture
import numpy as np

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import spacy
import langdetect

# Create a new chatbot
chatbot = ChatBot('MyBot')

# Initialize the chatbot and recognizer
chatbot = ChatBot('MyBot')
recognizer = sr.Recognizer()

# Define the path where the user's speech will be stored
PATH = 'data/'

# Define the number of components in the GMM model
N_COMPONENTS = 16

# Define the duration of each speech sample
SAMPLE_DURATION = 5  # seconds

# Define the sampling rate and chunk size for recording audio
RATE = 44100
CHUNK_SIZE = 1024

# Define a function to record speech and save it to a file
def record_speech(name):
    print(f"Please record {SAMPLE_DURATION} seconds of your speech.")
    with sr.Microphone() as source:
        audio = recognizer.record(source, duration=SAMPLE_DURATION)
    filename = os.path.join(PATH, name, f"{name}.wav")
    with open(filename, "wb") as f:
        f.write(audio.get_wav_data())
    print("Speech sample saved to:", filename)

# Define a function to train the speaker recognition model
def train_model(name):
    # Load the speech samples from disk
    files = os.listdir(os.path.join(PATH, name))
    speech_samples = []
    for file in files:
        if file.endswith('.wav'):
            filename = os.path.join(PATH, name, file)
            with sr.AudioFile(filename) as source:
                audio = recognizer.record(source)
            speech_samples.append(audio.get_array_of_samples())

    # Extract MFCC features from the speech samples
    mfccs = []
    for speech_sample in speech_samples:
        mfcc = librosa.feature.mfcc(np.asarray(speech_sample), sr=RATE, n_mfcc=13, hop_length=CHUNK_SIZE, n_fft=2048)
        mfccs.append(mfcc.flatten())
    mfccs = np.asarray

    

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on multiple corpora
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations",
              "chatterbot.corpus.spanish")

# Define a custom logic adapter that uses Spacy for NLP
class SpacyAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nlp = spacy.load('en_core_web_sm')

    def process(self, input_statement, additional_response_selection_parameters):
        doc = self.nlp(input_statement.text)
        for ent in doc.ents:
            input_statement.add_tags(ent.label_)
        return input_statement

# Add the Spacy adapter to the chatbot
chatbot.logic_adapters = [
    {
        "import_path": "SpacyAdapter",
        "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
        "response_selection_method": "chatterbot.response_selection.get_first_response"
    }
]

# Start the chatbot
while True:
    user_input = input("You: ")
    language = langdetect.detect(user_input)
    if language == 'en':
        response = chatbot.get_response(user_input)
    else:
        response = Statement('Lo siento, solo hablo inglés por ahora.')
    print("Bot: ", response)
