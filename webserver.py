import os
import requests
from flask import Flask, render_template, request

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route('/')
def hello_world():
    return render_template("index.html") 
@app.route('/blog/8-experiments-in-motivation')
def exper():
	return render_template("8ExperimentsinMotivation.html")

@app.route('/contact')
def contact():
	return render_template("contact_us.html")
@app.route('/index')
def index():
	return render_template("index.html")
@app.route('/about')
def about():
	return render_template("about_us.html")
@app.route('/blog/a-mindful-shift-of-focus')
def mind():
	return render_template("AMindfulShiftofFocus.html")
@app.route("/blog/how-to-develop-an-awesome-sense-of-direction")
def how():
	return render_template("HowtoDevelopanAwesomeSenseofDirection.html")
@app.route("/blog/training-to-be-a-good-writer")
def train():
	return render_template("TrainingtoBeaGoodWriter.html")
@app.route("/blog/what-productivity-systems-wont-solve")
def what():
	return render_template("WhatProductivitySystemsWon'tSolve.html")

@app.route('/contact',methods=['GET'])
def contact_display():
    return render_template("contact_us.html",notifications=[])

@app.route('/contact', methods=['POST'])
def send_email():
	message = request.form.get("message")
	subject = request.form.get("subject")
	name = request.form.get("name")
	email = request.form.get("email")

	message = message + "From: " + name + " Email: " + email
	notifications = []

	data = {
		'from': os.environ["INFO253_MAILGUN_FROM_EMAIL"],
		'to': os.environ["INFO253_MAILGUN_TO_EMAIL"],
		'subject': subject,
		'text': message,
	}
	auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])

	r = requests.post(
		'https://api.mailgun.net/v3/{}/messages'.format(os.environ["INFO253_MAILGUN_DOMAIN"]),
		auth=auth,
		data=data)
	if r.status_code == requests.codes.ok:
		notifications.append("Hi " + name + ", your message has been sent.")
	else:
		notifications.append("Your message has not been sent. Please try again later")

	return render_template("contact_us.html", notifications=notifications)
