from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)


@app.route("/save_data", methods=["POST"])
def save_data():
    return ...
