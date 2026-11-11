# PyTorch is a module used for building and training neural
# networks.
import torch

# torch.nn is used for loading a Neural Network module.
# Think of it as a neural network toolkit. 'nn' is an alias
# or alternative name which makes it easier to access this
# module.
import torch.nn as nn

# torch.optim loads the optimization algorithms which are
# important for the learning process.
import torch.optim as optim

# Import the Tokenizer class into this namespace.
from data.tokenizer import Tokenizer

import json

# Build a neural network from scratch (without pretrained models)
# that accepts a sentence as input and generates an appropriate
# text response.

# A neural network is a model that used in artificial intelligence
# teaches computers to process data and recognise complex patterns.

# Example interaction:
# User speaks: "Hello, how are you?"

# speech_recognition.py converts audio into text.
# Output: "Hello, how are you?"

# response_generation.py determines an appropriate textual response.
# Output: "I'm doing well, thank you!"

# speech_synthesis.py converts the text into audio.

# Load the conversational training data from a JSON file.

# The with statement is a context manager because it guarantees
# that the file will be automatically closed in a way that
# prevents memory leaks.

# A file object is a link between this Python program and a
# particular file. In this case, that file is conversations.json.

# The second argument to open() is "r" which means that the file
# is being opened for reading.

# encoding="utf-8" specifies encoding to ensure special characters
# like emojis or foreign alphabet characters are read correctly.
with open("data/conversations.json", "r", encoding="utf-8") as file_obj:
    # Load the JSON data from the file and convert it into Python
    # objects.
    conversation_data = json.load(file_obj)


class Encoder:
    pass


class Decoder:
    pass