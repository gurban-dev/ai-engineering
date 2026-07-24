import random

# In this program, the AI is trying to find the cat.

# Part 1: Create the Training Data
training_data = [
    {"x": 2, "y": 3},
    {"x": 6, "y": 8},
    {"x": 4, "y": 5},
]

# Part 2: Making Random Predictions

# At this point, the AI has not learned anything.
# It simply guesses.

# The random.randint() function generates a random number between
# and including the lower and upper bounds.
# random.randint(lower (inclusive), upper (inclusive))

predicted_x = random.randint(0, 10)
predicted_y = random.randint(0, 10)