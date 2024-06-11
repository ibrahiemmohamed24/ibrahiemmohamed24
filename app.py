from flask import Flask, request, render_template
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    mobile = request.form["mobile"]
    save_to_file(name, mobile)
    return "Form submitted successfully!"

def save_to_file(name, mobile):
    with open("form_data.txt", "a") as file:
        file.write(f"Name: {name}, Mobile: {mobile}\n")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
