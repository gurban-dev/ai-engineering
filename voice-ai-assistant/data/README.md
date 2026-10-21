data/raw/ contains our original text data.

Before we can give this data to the model, we need to:
Tokenize the text -> break the text into tokens.
Convert the tokens into IDs -> replace each token with a number.

Pipeline:
data/raw/tiny_dataset.txt
        ↓
    tokenizer.py
        ↓
data/processed/
        ↓
    dataset.py
        ↓
   training examples
        ↓
     model.py
        ↓
     training