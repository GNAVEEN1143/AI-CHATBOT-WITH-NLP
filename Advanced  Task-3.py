import nltk
from nltk.chat.util import Chat, reflections

# Define the chatbot pairs: pattern and responses

pairs = [
    (r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! How can I help?"]),
    (r"what is your name?", ["I am a simple chatbot.", "I'm just a bot, no fancy name yet!"]),
    (r"how are you?", ["I'm doing great, thanks for asking!", "I'm just a bot, but I'm doing fine!"]),
    (r"what can you do?", ["I can answer your questions or have a simple conversation.", "I can chat with you and provide helpful information."]),
    (r"(.*) your favorite color?", ["I don't have preferences, but I like all colors!", "Colors are fun, but I don't have a favorite."]),
    (r"(.*) (weather|temperature|climate)(.*)", ["I'm not sure about the weather, but you can check it online!"]),
    (r"bye|goodbye", ["Goodbye! Have a nice day!", "Bye! Take care!"]),
    (r"(.*)", ["I'm sorry, I didn't quite understand that.", "Can you please clarify?"])
]

# Define the chatbot class
class SimpleChatbot:
    def __init__(self):
        # Initialize the chatbot with pairs and reflections
        self.chatbot = Chat(pairs, reflections)
    
    def start_chat(self):
        print("Hello! I am your chatbot. Type 'bye' to exit.")
        while True:
            # Take user input
            user_input = input("You: ")
            # If the user says 'bye', exit the loop
            if user_input.lower() in ['bye', 'goodbye']:
                print("Chatbot: Goodbye! Have a nice day!")
                break
            # Respond to the user input
            response = self.chatbot.respond(user_input)
            print(f"Chatbot: {response}")

# Main function to start the chatbot
if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.start_chat()
