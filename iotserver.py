from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Server is running! Use /store-data to send data."})

@app.route('/store-data', methods=['POST'])
def store_data():
    data = request.get_json()
    print("Received data:", data)  # Logs for debugging
    return jsonify({"status": "success", "received": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
