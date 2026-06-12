import json

with open("keywords.json", "r", encoding="utf-8") as file:
    keywords = json.load(file)

def get_reply(comment):
    comment = comment.lower()

    for keyword, reply in keywords.items():
        if keyword in comment:
            return reply

    return "Thank you for your comment 😊"

if __name__ == "__main__":
    comment = input("Enter Comment: ")
    print("Auto Reply:", get_reply(comment))