import json

# Load keywords
with open("keywords.json", "r") as file:
    keywords = json.load(file)

comment = input("Enter Comment: ").lower()

reply_found = False

for keyword, reply in keywords.items():
    if keyword in comment:
        print("Auto Reply:", reply)
        reply_found = True
        break

if not reply_found:
    print("Auto Reply: Thank you for your comment 😊")