# Import the os module so we can access environment variables.
import os

# Import load_dotenv so we can load the .env file.
from dotenv import load_dotenv

# Import the OpenAI client.
from openai import OpenAI

# Load the environment variables from the .env file.
load_dotenv()

# Retrieve the API key from the environment variables.
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Create a client that communicates with the AI server.
client = OpenAI(api_key=OPENAI_API_KEY)

# Display a welcome message.
print("=" * 50)
print("AI Customer Support Assistant")
print("=" * 50)

# Ask for the customer's name once.
customer_name = input("Customer name: ")

# Continue helping customers until the user decides to quit.
while True:

    # Ask the user to enter a customer's question.
    customer_message = input(
        "\nEnter the customer's message (or type 'quit' to exit): "
    )

    # Check whether the user wants to end the program.
    if customer_message.lower() == "quit":
        print("\nGoodbye!")
        break

    # Tell the user that the request is being sent.
    print("\nSending request to the AI...")

    # Build a multi-line prompt for the AI.
    prompt = f"""
You are an experienced customer support representative.

The customer's name is {customer_name}.

Your job is to answer the customer's question.

Requirements:
- Be polite.
- Be professional.
- Be friendly.
- Use simple English.
- Avoid technical words whenever possible.
- Keep your response under 150 words.
- Begin your response by greeting the customer by name.

Customer's message:
{customer_message}
"""

    # Send the prompt to the AI and store the response.
    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    # Tell the user that the response has arrived.
    print("Response received!\n")

    # Display the AI's response.
    print(response.output_text)

    # Print a separator before the next conversation.
    print("\n" + "-" * 50)