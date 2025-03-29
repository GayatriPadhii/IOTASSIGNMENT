from flask import Flask, request, jsonify

app = Flask(__name__)

# Store received data
parking_data = []

@app.route('/store-data', methods=['POST'])
def store_data():
    data = request.get_json()
    parking_data.append(data) 
    print("Received data:", data)
    return jsonify({"status": "success", "received": data}), 200

@app.route('/view-data', methods=['GET'])
def view_data():
    return jsonify(parking_data) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
