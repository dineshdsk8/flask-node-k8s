from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Backend Running"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    print("DATA RECEIVED:", data)

    return jsonify({
        "message": "Data received successfully",
        "name": data.get("name"),
        "email": data.get("email")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)