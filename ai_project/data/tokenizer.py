import re
# Re stands for regular expression. 
# # Regular expressions are patterns that describe text we want to find.
# \w+ finds one or more word characters, such as letters or numbers.
# [^\w\s] finds one character that is not a word character or whitespace.
# The | means "or", so we find either a word or a punctuation character.


# The purpose of a tokenizer:
# Break text into smaller pieces called tokens so that the AI
# model can process the text.

# A tokenizer is not a type of AI.

# The tokenizer will:
# 1. Take the raw text.
# 2. Split the text into words and punctuation.
# 3. Build a vocabulary.
# 4. Convert tokens into integer IDs.
# 5. Convert IDs back into tokens.

# The tokenizer sits between the raw text and the neural network.

# Pipeline:


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
        # Use a regular expression to split the text into tokens.
        # Regular expressions are patterns that describe text we want to find.
        # \w+ finds one or more word characters, such as letters or numbers.
        # [^\w\s] finds one character that is not a word character or whitespace.
        # The | means "or", so we find either a word or a punctuation character.
        tokens = re.findall(r"\w+|[^\w\s]", text)

        for token in tokens:
            if token not in self.token_to_id:
                # Assign a unique ID to the token.
                token_id = len(self.token_to_id)
                self.token_to_id[token] = token_id
                self.id_to_token[token_id] = token
        return tokens

raw_text = [
    "Hello, world!",
    "Hello Python.",
    "Python isgreat!"
]

tokenizer = Tokenizer()

tokens = tokenizer.tokenize(raw_text[2])

print("tokens:", tokens)


# 1. Create a vocabulary of known words.

# A raw corpus is a collection of unedited text using in natural
# language processing.
raw_corpus = """
this is great
this is really great
the movie is great
the food is great
this example is useful
we are building a tokenizer
the tokenizer should learn useful tokens
this is another great example
"""

# 2. Split each word into individual characters.

def split_into_characters(text: str):
    words = text.lower().split()

    list_of_word_lists = []

    for word in words:
        # Each word will be converted into a list where each character
        # in a word becomes an item/element in the list.
        word_as_list = list(word)

        list_of_word_lists.append(word_as_list)

    return list_of_word_lists

print("\nraw_corpus:", raw_corpus)

print("\nsplit_into_characters(raw_corpus):\n", split_into_characters(raw_corpus), sep="")