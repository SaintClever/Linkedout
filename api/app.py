from country.codes import country_codes
from currency.codes import currency_codes
from database.database import db_connection
from .api_methods.post import post
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/save_data", methods=["POST"])
def save_data():
    data = request.json

    try:
        if (
            request.is_json
            and data.get("location").casefold() in country_codes
            and data.get("currency").casefold() in currency_codes
        ):
            data["starting_salary"] = int(data.get("starting_salary"))
            data["max_salary"] = int(data.get("max_salary"))
            # post(db_connection, data)
            return jsonify({"message": "Data saved successfully"}), 201
        else:
            return jsonify({"error": f"Invalid data provided"}), 400
    except (AttributeError, ValueError, KeyError) as e:
        return jsonify({"error": f"Invalid data provided: {e}"}), 400


if __name__ == "__main__":
    app.run(debug=True)
