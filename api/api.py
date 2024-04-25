from job_boards.jobs_to_db import insert_job_data
from database.database import db_connection
from flask import Flask, request, jsonify


app = Flask(__name__)


# {
#     "company_name": "linkedout",
#     "job_title": "Python Developer",
#     "job_href": "https://www.linkedout.com/",
#     "location": "Remote",
#     "currency": "USD",
#     "starting_salary": 100000,
#     "max_salary": 750000
# }


@app.route("/save_data", methods=["POST"])
def save_data():
    data = request.json
    print(data)
    insert_job_data(db_connection, data)
    return jsonify({"message": "Data saved successfully"}), 201


if __name__ == "__main__":
    app.run(debug=True)
