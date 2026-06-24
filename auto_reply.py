import json
import random

with open("keywords.json", "r", encoding="utf-8") as file:
    keywords = json.load(file)

default_replies = [
    "Thank you for your comment 😊",
    "Thank you for your valuable feedback 🌱",
    "We appreciate your support 🌳",
    "Thank you for supporting Tree Kisan 🚜",
    "Your feedback is valuable to us 🌟"
]

def get_reply(comment):
    comment = comment.lower()

    for keyword, reply in keywords.items():
        if keyword.lower() in comment:
            return reply

    return random.choice(default_replies)

if __name__ == "__main__":
    comment = input("Enter Comment: ")
    print("Auto Reply:", get_reply(comment))