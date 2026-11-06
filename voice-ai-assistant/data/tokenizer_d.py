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


# Notice how there are at least two empty lines above the class
# header (class Tokenizer).
class Tokenizer:
    
    # The purpose of the __init__() method is to initialise the
    # state of an object.

    # self refers to an instance of this class.
    def __init__(self):

        # Special tokens used by the neural network.

        # <SOS>: Start of Sequence - Marks the beginning of a text
        #                            sequence or sentence.
        # <PAD>: Padding - A placeholder token used to make all sequences
        #                  in a batch the same length.
        # <EOS>: End of Sequence - Marks the conclusion of a text sequence
        #                          or sentence.
        # <UNK>: Unknown - Replaces any word or token that is not present in
        #                  the model's vocabulary.
        self.special_tokens = ["<SOS>", "<PAD>", "<EOS>", "<UNK>"]

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
        self.token_to_id = {
            token: index
            for index, token in enumerate(self.special_tokens)
        }

        # id_to_token will eventually look like:
        # {
        #     0: ".",
        #     1: "cat",
        #     2: "The",
        #     5: "sat"
        # }

        # It answers:
        # What token does this number represent?
        self.id_to_token = {
            index: token
            for token, index in self.token_to_id.items()
        }

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

    def fit(self, texts):

        # Go through each text in the training dataset.
        for text in texts:

            # Split the text into individual tokens.
            tokens = self.tokenize(text)

            # Check each token to see if it is already in the vocabulary.
            for token in tokens:

                # Add the token only if it is not already in the vocabulary.
                if token not in self.token_to_id:

                    # Assign the next available integer as the token's ID.
                    token_id = len(self.token_to_id)

                    # Store the token and its corresponding ID.
                    self.token_to_id[token] = token_id

                    # Store the ID and its corresponding token.
                    self.id_to_token[token_id] = token

    def encode(self, text):

        # Split the input text into individual tokens.
        tokens = self.tokenize(text)

        # Convert each token into its corresponding integer ID.
        # Use the <UNK> token ID if a token is not in the vocabulary.
        token_ids = [
            self.token_to_id.get(token, self.token_to_id["<UNK>"])
            for token in tokens
        ]

        # Return the list of integer IDs.
        return token_ids

    def decode(self, token_ids):

        # Create an empty list to store the decoded tokens.
        tokens = []

        # Go through each integer ID in the input list.
        for token_id in token_ids:

            # Convert the integer ID back into its corresponding token.
            # Use <UNK> if the ID does not exist in the vocabulary.
            token = self.id_to_token.get(token_id, "<UNK>")

            # Skip special tokens such as <SOS>, <EOS>, <PAD>, and <UNK>.
            if token in self.special_tokens:
                continue

            # Attach punctuation to the end of the previous token.
            if token in [".", ",", "!", "?", ";", ":"]:
                if tokens:
                    tokens[-1] += token

            # Add regular tokens to the list.
            else:
                tokens.append(token)

        # Join the tokens with spaces to reconstruct the text.
        return " ".join(tokens)

# The code in the if block will execute only if this file is
# not being imported.
if __name__ == "__main__":
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