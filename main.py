# from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates
# from pydantic import BaseModel
# from fastapi.staticfiles import StaticFiles
# from chat import get_completion_from_messages,collect_messages_text

# app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")

# class Message(BaseModel):
#     content: str

# @app.get("/")
# def home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/chat")
# async def chat(message: Message):
#     user_message = message.content
#     response = collect_messages_text(user_message)

#     return {"message": response}

# @app.post("/process_voice")
# async def process_voice(voice_input: dict):
#     # print(voice_input)
#     text = voice_input.get('input')
#     # Process the voice input as needed
#     # print("Voice input:", text)
#     response = collect_messages_text(text)
#     # print(response)
#     return {"message": response}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, port=8000)

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
