# 2. Magic 8 Ball Extension
import random

# List of possible Magic 8 Ball responses
responses = [
    "Yes, definitely!",
    "It is decidedly so.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Very doubtful."
]

print("Welcome to the Magic 8 Ball! (Type 'quit' to stop)")

while True:
    question = input("\nAsk the Magic 8 Ball a question: ")
    if question.lower() == "quit":
        print("Goodbye!")
        break
    else:
        print("Magic 8 Ball says:", random.choice(responses))
