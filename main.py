from flask import Flask, render_template, request
import requests
from twilio.rest import Client




app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generic')
def generic():
    return render_template("generic.html")

@app.route('/data', methods=["GET", "POST"])
def data():
    name = request.form.get("name")
    email = request.form.get("email")
    messages = request.form.get("message")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"{name} wants to get in touch with you. His/Her email is {email}.\n The message is {messages}.",
        from_=twilio_number,
        to="+917760542546"
    )
    print(message.status)
    return render_template("index.html")
app.run(debug=True)
