import random
import spacy
import webbrowser


nlp = spacy.load("en_core_web_sm")

intents = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
            "responses": ["Hello! How are you today?", "Hi there! Glad to chat with you."]
        },
        {
            "tag": "feeling",
            "patterns": ["how are you", "how's it going", "what's up"],
            "responses": ["I'm doing great! Thanks for asking. How about you?", "All good here, what about you?"]
        },
        {
            "tag": "name",
            "patterns": ["what is your name", "who are you", "your name"],
            "responses": ["I'm your friendly chatbot 🤖", "You can call me ChatBuddy!"]
        },
        {
            "tag": "age",
            "patterns": ["how old are you", "your age"],
            "responses": ["I'm timeless 😎", "Age is just a number, but I'm quite new!"]
        },
        {
            "tag": "hobby",
            "patterns": ["what do you do", "your hobby", "what's your favorite thing"],
            "responses": ["I love chatting with people like you!", "My hobby is helping humans with information."]
        },
        {
            "tag": "goodbye",
            "patterns": ["bye", "goodbye", "exit", "quit"],
            "responses": ["Goodbye! Have a nice day 😊", "See you later! Take care."]
        }
    ]
}

def chatbot_response(user_input):
    doc = nlp(user_input.lower())
    user_tokens = [token.lemma_ for token in doc]

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            pattern_doc = nlp(pattern.lower())
            pattern_tokens = [token.lemma_ for token in pattern_doc]
            if any(word in user_tokens for word in pattern_tokens):
                return random.choice(intent["responses"])

    print("🤖 Chatbot: Sorry, I didn’t understand that. I’m taking you to Google..")
    webbrowser.open(f"https://www.google.com/search?q={user_input}")
    return "🔎 Opening Google search for your query..."


print("🤖 Chatbot: Hi! I'm your chatbot. Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("🤖 Chatbot:", chatbot_response(user_input))
        break
    print("🤖 Chatbot:", chatbot_response(user_input))
