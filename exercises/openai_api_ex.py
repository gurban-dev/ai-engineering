"""
Scenario

You work for a company that sells computers.

Every day, customers contact your company with questions and problems.
Instead of writing every response yourself, you are going to build an
AI-powered customer support assistant.

Your job is to write a Python program that sends the customer's message
to the AI and displays the AI's response.

------------------------------------------------------------
Requirements
------------------------------------------------------------

Your customer_support.py program MUST:

1. Create a .env file.

2. Inside .env, write an appropriate environment variable name for
   your OpenAI API key. This is where your API key will be stored.

3. Load the API key from a .env file.

4. Create an OpenAI client.

5. Ask the user to enter a customer's message.

6. Store the customer's message in a variable named:

   customer_message

7. Send the message to the AI.


The AI should act as:

An experienced customer support representative.

The AI should:

• Be polite.
• Be professional.
• Be friendly.
• Answer the customer's question.
• Keep the response under 150 words.

6. Store the AI's response in a variable named:

   response

7. Print the AI's response.

------------------------------------------------------------
Example
------------------------------------------------------------

User Input

My laptop battery only lasts for one hour.
What should I do?

Example Output

Thank you for contacting us.

I'm sorry to hear that your laptop's battery life is much shorter
than expected. Please try reducing your screen brightness,
closing unused applications, and enabling battery saver mode.

If the problem continues, please contact our support team so we
can help determine whether your battery needs to be replaced.

Please let us know if you have any additional questions.

------------------------------------------------------------
Challenge 1
------------------------------------------------------------

Before sending the request to the AI, print:

Sending request to the AI...

After receiving the response, print:

Response received!

------------------------------------------------------------
Challenge 2
------------------------------------------------------------

Allow the user to ask more than one question.

Use a while loop.

The program should continue running until the user types:

quit

------------------------------------------------------------
Challenge 3
------------------------------------------------------------

Improve your prompt.

Tell the AI to:

• Use simple English.
• Be encouraging.
• Avoid technical words whenever possible.

------------------------------------------------------------
Bonus Challenge
------------------------------------------------------------

Ask the user for the customer's name.

Example:

Customer name:

Then include the customer's name inside the prompt so that the AI
greets the customer personally.

Example:

Hello Sarah,

Thank you for contacting us...

------------------------------------------------------------
Things You Must Use
------------------------------------------------------------

Your solution must include:

• import
• load_dotenv()
• os.environ.get()
• OpenAI()
• input()
• Variables
• client.responses.create()
• print()
• A multi-line f-string prompt
• A while loop

------------------------------------------------------------
Success Checklist
------------------------------------------------------------

□ Loads the API key from the .env file.

□ Creates an OpenAI client.

□ Asks the user for a customer's message.

□ Sends the message to the AI.

□ Prints the AI's response.

□ Allows the user to ask multiple questions until the user types
  "quit".

□ Uses clear above-line comments that explain every major part of
  the program.
"""