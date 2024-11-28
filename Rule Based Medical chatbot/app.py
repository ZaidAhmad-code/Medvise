from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rule-based chatbot responses
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm here to help! How can I assist you?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you ask something else?"

# Flask route for the main page
@app.route("/")
def home():
    return render_template("index.html")

# Flask route for handling messages
@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    response = chatbot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
