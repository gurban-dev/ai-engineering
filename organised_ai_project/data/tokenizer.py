import re

# The purpose of a tokenizer:
# Break text into smaller pieces called tokens so that the AI
# model can process the text.

# The tokenizer will:
# 1. Take the raw text.
# 2. Split the text into words and punctuation.
# 3. Build a vocabulary.
# 4. Convert tokens into integer IDs.
# 5. Convert IDs back into tokens.

# The tokenizer sits between the raw text and the neural network.

# Pipeline:
# Raw text
#    ↓
# tokenize()
#    ↓
# ["Hello", ",", "Python", "!"]
#    ↓
# build_vocabulary()
#    ↓
# {
#     "Hello": 0,
#     ",": 1,
#     "Python": 2,
#     "!": 3,
#     ...
# }
#    ↓
# encode()
#    ↓
# [0, 1, 2, 3]
#    ↓
# decode()
#    ↓
# ["Hello", ",", "Python", "!"]


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

    def tokenize(self, text):
        tokenized_lines = list()

        for line in text:
            # Regular expressions are patterns that describe text we want to find.
            # \w+ finds one or more word characters, such as letters or numbers.
            # [^\w\s] finds one character that is not a word character or whitespace.
            # The | means "or", so we find either a word or punctuation character.
            tokens = re.findall(r"\w+|[^\w\s]", line)

            tokenized_lines.append(tokens)

        return tokenized_lines

raw_text = [
    "Hello, world!",
    "Hello Python.",
    "Python is great!"
]

tokenizer = Tokenizer()

tokenizer.tokenize(text=raw_text)