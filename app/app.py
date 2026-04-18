from flask import Flask
from calculator import add

app = Flask(__name__)

@app.route("/")
def home():
    return f"CI/CD Demo 🚀 2 + 3 = {add(2,3)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)