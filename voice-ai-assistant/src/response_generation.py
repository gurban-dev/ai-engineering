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

    print("conversation_data:", conversation_data)

# Encoder reads the user's sentence.
# Suppose the tokenizer converts:
# Hello how are you

# into:
# [12, 8, 25, 41]
class Encoder(nn.Module):
    # vocab_size is the total number of unique tokens in the
    # vocabulary.

    # embedding_dim gets its name from representing the dimensions
    # of an embedding vector.

    # An embedding is a numerical representation of something.
    # E.g. A word or token.

    # The word Hello becomes the integer 4.

    # The dimension describes the number of values needed to
    # represent a point.
    # 1 dimension: [0.5]
    # 2 dimensions: [0.5, 0.8]
    # 128 dimensions: A vector containing 128 numerical values.

    # hidden_dim is the number of values maintained in the LSTM's
    # hidden state.

    # LSTM stands for Long Short-Term Memory and this is a type
    # of Recurrent Neural Network (RNN) designed to process
    # sequential data while preserving information from earlier
    # parts of the sequence.

    # The LSTM's hidden state is a collection of numerical values
    # that represents information the LSTM has remembered from the
    # sequence it has processed.
    def __init__(self, vocab_size, embedding_dim, hidden_dim):
        pass


class Decoder:
    pass