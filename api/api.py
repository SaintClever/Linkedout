from database.database import db_connection
from .data_to_db import insert_job_data
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/save_data", methods=["POST"])
def save_data():
    data = request.json
    insert_job_data(db_connection, data)
    return jsonify({"message": "Data saved successfully"}), 201


if __name__ == "__main__":
    app.run(debug=True)
