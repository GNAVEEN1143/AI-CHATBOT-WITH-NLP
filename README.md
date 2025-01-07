# AI-CHATBOT-WITH-NLP

Name: GADAPA NAVEEN KUMAR

Company: CODTECH IT SOLUTIONS

ID: CT0806AW

Domain: Python Programming

Duration: December 2024 to January 2025

Mentor: N.Santosh


Project: AI-CHATBOT-WITH-NLP

Overview:

The code is a simple chatbot implementation using the `nltk` library's `Chat` class. Here's a detailed overview of how the program works:

### Key Components:

1. **Imports**:
   - `nltk`: A popular Natural Language Processing (NLP) library that includes tools for text processing, tokenization, and more.
   - `Chat` and `reflections` from `nltk.chat.util`: These are part of the `nltk` library for creating rule-based chatbots. 
     - `Chat`: The class that handles the pattern-response pairs and generates responses.
     - `reflections`: A dictionary that helps with simple transformation of input-output, such as reflecting pronouns (e.g., "I" becomes "you", "my" becomes "your").

2. **Chatbot Pattern-Response Pairs** (`pairs`):
   - The `pairs` list contains tuples where each tuple has a regular expression (regex) pattern and a list of potential responses.
   - The regular expressions define patterns that the chatbot will look for in the user’s input, and for each matching pattern, the chatbot selects one of the predefined responses.
   
   Some example pairs include:
   - `(r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! How can I help?"])`
     - If the user greets the bot with "hi", "hello", or "hey", the bot will respond with a greeting.
   - `(r"what is your name?", ["I am a simple chatbot.", "I'm just a bot, no fancy name yet!"])`
     - If the user asks the bot's name, it will respond with a generic response.
   - `(r"(.*) (weather|temperature|climate)(.*)", ["I'm not sure about the weather, but you can check it online!"])`
     - If the user asks about the weather, the bot gives a simple response indicating it cannot provide weather data.

   The last pair `(r"(.*)", ["I'm sorry, I didn't quite understand that.", "Can you please clarify?"])` acts as a catch-all for any unrecognized inputs, and the bot will respond with a generic clarification message.

3. **SimpleChatbot Class**:
   - **`__init__()`**: Initializes the chatbot by creating an instance of the `Chat` class from `nltk.chat.util`, passing the `pairs` and `reflections` as arguments. This sets up the chatbot to respond according to the defined patterns.
   - **`start_chat()`**: 
     - This method handles the interaction between the user and the chatbot.
     - The chatbot welcomes the user with a greeting and then enters a loop to repeatedly take input from the user.
     - The user can type their message, and if it matches any defined pattern, the bot will respond accordingly.
     - The loop ends when the user types "bye" or "goodbye", at which point the chatbot says goodbye and exits.

4. **Main Program**:
   - **`if __name__ == "__main__":`**: This block ensures that the chatbot starts when the script is executed directly.
   - The program creates an instance of the `SimpleChatbot` class and then starts the chat by calling `chatbot.start_chat()`.

### Example Interaction:

- **User**: `hello`
- **Chatbot**: `Hello! How can I assist you today?`

- **User**: `What's your favorite color?`
- **Chatbot**: `I don't have preferences, but I like all colors!`

- **User**: `What's the weather like?`
- **Chatbot**: `I'm not sure about the weather, but you can check it online!`

- **User**: `bye`
- **Chatbot**: `Goodbye! Have a nice day!`

### Points to Note:

- **Regex Patterns**: The regular expressions are simple and look for specific keywords or phrases (e.g., "hi", "hello", "what is your name?"). The bot's ability to understand is limited by these patterns.
- **Reflections**: The `reflections` dictionary helps to convert user inputs into bot-friendly responses, but this is not heavily used in this example.
- **Extendability**: You can easily extend the chatbot by adding more patterns and responses. For example, you can include more detailed conversational logic, or integrate external APIs for more complex functionality like fetching weather data.
- **Catch-all Response**: The last pair (`(r"(.*)", ...)`) ensures that the bot can always respond even if it doesn't recognize the input.

### Summary:

This is a basic chatbot that uses predefined patterns and responses to simulate conversation. It works in a simple rule-based manner, matching user inputs to predefined patterns and providing appropriate responses. The chatbot will continue to interact with the user until the user types "bye" or "goodbye". This type of chatbot is useful for simple, predefined conversations but can be enhanced with more complex features like NLP processing, machine learning, or external data integration.

OUTPUT:

![Screenshot 2025-01-07 163446](https://github.com/user-attachments/assets/f2ddc37d-0ad3-408c-9864-09ab12c9b5ea)
