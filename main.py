from flask import Flask, request, render_template, jsonify
from chat import get_completion_from_messages, collect_messages_text

app = Flask(__name__)

# Define your static and templates directories
app.static_folder = 'static'
app.template_folder = 'templates'

class Message:
    def __init__(self, content):
        self.content = content

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    message = Message(request.json['content'])
    response = collect_messages_text(message.content)
    return jsonify({"message": response})

@app.route('/process_voice', methods=['POST'])
def process_voice():
    voice_input = request.json
    text = voice_input.get('input')
    response = collect_messages_text(text)
    return jsonify({"message": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)
