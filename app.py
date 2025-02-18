from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is a test site!"

@app.route("/verify")
def verify():
    discord_id = request.args.get("id")
    if not discord_id:
        return "Invalid request", 400
    user_ip = request.remote_addr
    return f"User {discord_id} verified with IP {user_ip}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
