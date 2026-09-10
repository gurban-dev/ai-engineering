Goal:
Build a small language model that learns to predict the next token
in a sequence of text.

Input:
A sequence of tokens (a token is a piece of text that an AI model
treats as one unit).

Output:
A probability distribution over the vocabulary for the next token.

A probability distribution is a way of assigning a probability to
every possible outcome.

Suppose our vocabulary contains only four tokens:
["The", "cat", "sat", "ate", "dog", "."]

We assign each token an ID:
"The" -> 0
"cat" -> 1
"sat" -> 2
"ate" -> 3
"dog" -> 4
"."   -> 5

So:
"The cat sat."

becomes:
"The cat sat."

After seeing:
"The cat"

the model might output:
the  -> 0.02
cat  -> 0.01
dog  -> 0.03
sat  -> 0.80
ran  -> 0.14

These numbers are probabilities because:
0.02 + 0.01 + 0.03 + 0.80 + 0.14 = 1.00

Training:
Self-supervised next-token prediction.

Self-supervised next-token prediction means the model learns by looking at
text and trying to guess the next token. The text itself tells the model
whether its guess was correct.

Success criterion:
The model's validation loss decreases during training.

Loss is a numerical measurement of how wrong the model's predictions are.