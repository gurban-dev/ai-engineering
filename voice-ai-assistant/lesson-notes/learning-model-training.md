# Small Language Model: Next-Token Prediction

## Goal

Build a small language model that learns to predict the next token in a sequence of text.

## Input

A sequence of tokens. A token is a piece of text that an AI model treats as one unit.

## Output

A probability distribution over the vocabulary for the next token. A probability distribution assigns a probability to every possible outcome, and all probabilities must sum to 1.

## Tokenization

Suppose our vocabulary contains the following tokens:

```python
["The", "cat", "sat", "ate", "dog", "."]
```

Each token receives a unique ID:

| Token | ID |
|---|---:|
| The | 0 |
| cat | 1 |
| sat | 2 |
| ate | 3 |
| dog | 4 |
| . | 5 |

The sentence `The cat sat.` becomes the token ID sequence:

```python
[0, 1, 2, 5]
```

## Example Prediction

After receiving `The cat`, the model might predict the following probabilities:

| Next token | Probability |
|---|---:|
| The | 0.02 |
| cat | 0.01 |
| dog | 0.03 |
| sat | 0.80 |
| ran | 0.14 |

The probabilities sum to 1.00, and the model assigns the highest probability to `sat`.

*Note: The example includes `ran`, which is not in the original vocabulary. A real model must include every possible predicted token in its vocabulary.*

## Training

Use **self-supervised next-token prediction**. The model learns from text by predicting the next token and comparing its prediction with the actual next token in the training data.

## Success Criterion

The model's **validation loss decreases during training**.

Loss measures how incorrect the model's predictions are. A decreasing validation loss indicates that the model is improving its next-token predictions on unseen text.