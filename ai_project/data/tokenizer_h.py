import re

# tiktoken tokenises text. Meaning it converts text into tokens that
# an AI language model can process.
import tiktoken

from wordsegment import load, segment

# Re stands for regular expression. 
# # Regular expressions are patterns that describe text we want to find.
# \w+ finds one or more word characters, such as letters or numbers.
# [^\w\s] finds one character that is not a word character or whitespace.
# The | means "or", so we find either a word or a punctuation character.

# Example with tiktoken:
encoding = tiktoken.get_encoding("cl100k_base")

text = "Hello, how are you?"

tokens = encoding.encode(text)

print("tokens:", tokens)

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

        # Load the dictionary data for word segmentation.
        # This is done once during initialization for efficiency.
        load()

    def tokenize(self, text):
        # Use a regular expression to split the text into initial tokens.
        initial_tokens = re.findall(r"\w+|[^\w\s]", text)
        
        final_tokens = []

        for token in initial_tokens:
            # We only want to segment potential words, not punctuation.
            # The \w+ pattern matches word characters (letters, numbers, underscore).
            if re.fullmatch(r'\w+', token):
                # The segment function splits concatenated words.
                # e.g., "hellopython" -> ["hello", "python"]
                # It also handles regular words, e.g., "hello" -> ["hello"]
                # The library automatically handles casing.
                segmented = segment(token)
                final_tokens.extend(segmented)
            else:
                # This is for punctuation and other non-word characters.
                final_tokens.append(token)

        for token in final_tokens:
            if token not in self.token_to_id:
                # Assign a unique ID to the token.
                token_id = len(self.token_to_id)

                self.token_to_id[token] = token_id
                self.id_to_token[token_id] = token

        return final_tokens

input_ = str(input("\nEnter a string to tokenize: "))

raw_text = [
    # Added for demonstration
    input_
]

tokenizer = Tokenizer()

# Test the new functionality
tokens = tokenizer.tokenize(raw_text[0])

print(f"Original text: '{raw_text[0]}'")
print(f"Tokens: {tokens}")

tokens_regular = tokenizer.tokenize(raw_text[0])

print(f"Original text: '{raw_text[0]}'")
print(f"Tokens: {tokens_regular}")