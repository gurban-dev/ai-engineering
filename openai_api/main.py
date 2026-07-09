'''
Python Program

->

Internet

->

OpenAI

->

Answer

->

Python Program

1. Navigate into the directory where this Python program (main.py)
   is located.

2. Create a virtual environment.

   python -m venv <name_of_the_virtual_environment>

   python -m venv .venv

   The -m flag tells Python to run a module as a program.

   In this case, Python runs the venv module, which creates a
   virtual environment.

   .venv is the virtual environment folder that will be created.

   The folder is commonly named .venv because on Linux and macOS,
   names that begin with a . are treated as hidden by default.

   Projects also usually add .venv to their .gitignore file so
   that the virtual environment is not committed to GitHub.

   A virtual environment is a folder that contains its own Python
   interpreter and the packages that your project needs.

3. Activate your virtual environment.

   . <virtual_env_name>/bin/activate

   . .venv/bin/activate

   . ./.venv/bin/activate

   ./ indicates that the .venv folder is located in the same
   directory.

   source .venv/bin/activate

4. Install the OpenAI Python package:

   pip install openai
'''

import os
from dotenv import load_dotenv

# From the module 'openai' import the class named OpenAI.
from openai import OpenAI

# Load the environment variables from the .env file.
load_dotenv()

# Retrieve the value of the OPENAI_API_KEY environment
# variable and assign it to OPENAI_API_KEY.
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# To test the previous line of code, a dummy value of abcde
# was assigned to the environment variable OPENAI_API_KEY.
print(f"OPENAI_API_KEY: {OPENAI_API_KEY}")

# A client is a software component that communicates with a
# web server by sending requests and receiving responses.

# Think of the client/frontend as the customer at a restaurant.
# The web server/backend is the kitchen staff.

# The waiter/waitress represents the API (Application
# Programming Interface). Just as the waiter acts as the
# intermediary between the customer and the kitchen, the
# API defines how requests and responses are exchanged
# between the client-side and the server-side.

# In most applications, the API exists on the backend (the server).

# Create an instance of the OpenAI class and assign it to a
# variable named 'client'.

# Calling the OpenAI class invokes its constructor
# (__init__), which initialises the new object.

# Whenever an instance of a class is created, the class is called
# and invokes its constructor.

# The following line calls the int class, which invokes its
# constructor to create an integer object.
# num = int(10)

# The OpenAI class accepts a parameter named api_key.

# This parameter can be seen in the OpenAI Python library's
# source code on GitHub:
# https://github.com/openai/openai-python/blob/main/src/openai/_client.py
client = OpenAI(api_key=OPENAI_API_KEY)


# Ask the OpenAI API to generate a response and assign it
# to the variable named 'response'.
response = client.responses.create(

    # Choose which OpenAI model should answer the question.
    model="gpt-5.5",

    # Send the prompt (the question or instruction) to the AI.
    input="""
    As an expert historian, please tell me what were
    the most significant events in human history.
    """
)

print(
    'response.output_text:\n',

    # Print only the text that the AI generated.
    response.output_text
)