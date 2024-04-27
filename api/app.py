import io
from country.codes import country_codes
from currency.codes import currency_codes
from database.database import db_connection
from .api_methods.post import post
from .api_methods.get import create_salary_plot
from flask import Flask, request, jsonify, send_file
import matplotlib

matplotlib.use("Agg")  # Set the backend before importing pyplot / Needed for send_file
app = Flask(__name__)


@app.route("/save_data", methods=["POST"])
def save_data():
    data = request.json

    try:
        # Validate data format
        # Ensure inserted locations and country codes are within country_codes and currency_codes
        if (
            request.is_json
            and data.get("location").casefold() in country_codes
            and data.get("currency").casefold() in currency_codes
        ):
            # Ensure salaries are integers
            data["starting_salary"] = int(data.get("starting_salary"))
            data["max_salary"] = int(data.get("max_salary"))

            # Insert data into the database
            post(db_connection, data)
            return jsonify({"message": "Data saved successfully"}), 201
        else:
            return jsonify({"error": f"Invalid data provided"}), 400
    except (AttributeError, ValueError, KeyError) as e:
        return jsonify({"error": f"Invalid data provided: {e}"}), 400


# NOTE: Incomplete
@app.route("/job_salaries", methods=["GET"])
def job_salaries():
    # Generate and save the plot to a bytes buffer
    buf = io.BytesIO()
    create_salary_plot().savefig(buf, format="png")
    buf.seek(0)

    # Send the buffer as a response
    return send_file(buf, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
