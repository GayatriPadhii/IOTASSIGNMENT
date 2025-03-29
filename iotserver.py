from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/store-data', methods=['POST'])
def store_data():
    data = request.get_json()
    print("Received data:", data)  # Debugging in logs
    return jsonify({"status": "success", "received": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
