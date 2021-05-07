from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "This is the second time running a propgram on docker container that too from Jenkins! Awesome.."
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
