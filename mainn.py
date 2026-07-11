import json
from groq import Groq
client = Groq(api_key="YOUR_GROQ_API_KEY")
FILE = "conversation.json"
def load_history():
    try:
       with open(FILE, "r") as file:
           return json.load(file)
    except:
       return []

def save_history(history):
    with open(FILE, "w") as file:
        json.dump(history, file, indent=4)

def chatbot(user_message):
    history = load_history()

    history.append({
        "role": "user",
        "content": user_message
        })
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=history
        )    

    reply = response.choices[0].message.content
    history.append({
        "role": "assistant",
        "content": reply
        })

    save_history(history)

    return reply

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    answer = chatbot(user_input)
    print("bot:", answer)
