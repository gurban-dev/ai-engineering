# The tokenizer will:
# 1. Take the raw text.
# 2. Split the text into words and punctuation.
# 3. Build a vocabulary.
# 4. Convert tokens into integer IDs.
# 5. Convert IDs back into tokens.

import re


# Notice how there are at least two empty lines above the class
# header (class Tokenizer).
class Tokenizer:
    # The purpose of the __init__() method is to initialise the
    # state of an object.

    # self refers to an instance of this class.
    def __init__(self):
        # When we create an instance of the Tokenizer class, two
        # empty dictionaries are initialised.

        # token_to_id will eventually look like:
        # {
        #     "The": 2,
        #     "cat": 1,
        #     "sat": 5,
        #     ".": 0
        # }

        # token_to_id answers:
        # What number represents this token?

        # A token is a piece of text that an AI model treats as one
        # unit.
        self.token_to_id = {}

        # id_to_token will eventually look like:
        # {
        #     0: ".",
        #     1: "cat",
        #     2: "The",
        #     5: "sat"
        # }

        # It answers:
        # What token does this number represent?
        self.id_to_token = {}

    