from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class UserForm(FlaskForm):
    company_name = StringField("Company Name")
    job_title = StringField("Job Title")
    job_href = StringField("Job Href")
    location = StringField("Location")
    currency = StringField("Currency")
    starting_salary = IntegerField("Starting Salary")
    max_salary = IntegerField("Max Salary")
    submit = SubmitField("Submit")
