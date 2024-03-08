from flask import Flask, request, redirect,jsonify,render_template
from datetime import datetime
from flask_cors import CORS
import json
import random

app = Flask(__name__)
CORS(app)
@app.route('/')
def main():
    return 'hi'
app.run()