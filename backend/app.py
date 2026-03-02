from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend Running Successfully"

@app.route("/login", methods=["POST"])
def login():
    return "Login Success"

if __name__ == "__main__":
    app.run(debug=True)