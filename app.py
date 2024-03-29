import whisper
import sys
import os
from flask import Flask
import json

app = Flask(__name__)
model = whisper.load_model("small")
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def index():
    model = whisper.load_model("tiny")
    result = model.transcribe("audio.mp3")
    return json.dumps({"text": result["text"].encode('utf-8').decode(sys.stdout.encoding)})
    # return json.dumps({"text": "Hello World!"})
