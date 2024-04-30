import os, io, base64
from dotenv import load_dotenv
from country.codes import country_codes
from currency.codes import currency_codes
from database.database import db_connection
from .api_methods.post import post
from .api_methods.get_method.get import salary_plot
from .api_methods.get_method.generate_df import df
from flask import Flask, request, jsonify, send_file, render_template, redirect, url_for
from .form.form import UserForm
import matplotlib

load_dotenv(".env")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Set the backend before importing pyplot / Needed for send_file
matplotlib.use("Agg")


@app.route("/", methods=["GET", "POST"])
def index():
    form = UserForm()

    if form.validate_on_submit():
        data = {
            "company_name": form.company_name.data,
            "job_title": form.job_title.data,
            "job_href": form.job_href.data,
            "location": form.location.data,
            "currency": form.currency.data,
            "starting_salary": form.starting_salary.data,
            "max_salary": form.max_salary.data,
        }
        post(db_connection, data)
        return redirect(url_for("index"))

    return render_template("index.html", form=form)


@app.route("/salary_api", methods=["GET"])
def salary_api():
    api = df.to_dict(orient="records")
    return jsonify(api)


@app.route("/save_data", methods=["POST"])
def save_data():
    data = request.json

    try:

        # Ensure inserted locations and country codes
        # are within country_codes and currency_codes
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


@app.route("/job_salaries", methods=["GET"])
def job_salaries():
    # Generate and save the plot to a bytes buffer
    buf = io.BytesIO()
    salary_plot.savefig(buf, format="png")
    buf.seek(0)

    # Send the buffer as a response
    # return send_file(buf, mimetype="image/png")

    # Encode the image data as base64
    image_data = base64.b64encode(buf.getvalue()).decode("utf-8")
    return render_template("image.html", image_data=image_data)


if __name__ == "__main__":
    app.run(debug=True)
