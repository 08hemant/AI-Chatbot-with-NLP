from flask import Flask, request, jsondiff
import spacy

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Initialize Flask app
app = Flask(__name__)

# Define responses
responses = {
    "greeting": "Hello! How can I assist you today?",
    "goodbye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I didn't understand that. Can you please rephrase?"
}

# Function to get the response based on intent
def get_response(intent):
    return responses.get(intent, responses["default"])

# Function to process user input and determine intent
def process_input(user_input):
    doc = nlp(user_input)
    if "hello" in doc.text.lower() or "hi" in doc.text.lower():
        return "greeting"
    elif "bye" in doc.text.lower() or "goodbye" in doc.text.lower():
        return "goodbye"
    else:
        return "default"

# Route for chatbot interaction
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    intent = process_input(user_input)
    response = get_response(intent)
    return jsondiff({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
