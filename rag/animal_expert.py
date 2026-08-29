# Stage One:
# An RAG system needs a knowledge source. animals.txt is the
# knowledge source in this case.

# The file_obj represents the connection between this Python
# program and the animals.txt file that is being opened for
# reading only.

# with open() acts as a context manager in Python by utilising
# the with statement to automatically handle the closing of the
# the file object. Without the with statement, file_obj.close()
# would have needed to be called to close the file object.

# The second argument, "r" indicates that "animals.txt" was
# opened for reading only.
with open("animals.txt", "r") as file_obj:
    # Reading the content from the file.
    animals = file_obj.read()

# print(f"animals:\n{animals}")

# Stage Two:
# Have the user ask a question.
question = input("Ask a question about animals: ")

print(f"\nYou asked: {question}\n")

# The question and the knowledge source need to be connected.
# This is the retrieval problem.

# Stage Three:
# Build a retriever.

words = question.lower().split()

for word in words:
    if word in animals.lower():
        print(f"Information has been found in the knowledge "
              f"source about: {word}")
    else:
        print(f"Information was not found in the knowledge "
              f"source about: {word}")