import whisper
import sys
import os
from flask import Flask

app = Flask(__name__)
model = whisper.load_model("small")
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def index():
    model = whisper.load_model("small")
    result = model.transcribe("audio.mp3")
    return ( result["text"].encode('utf-8').decode(sys.stdout.encoding))
