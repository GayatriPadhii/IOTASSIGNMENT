from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update():
    distance = request.form.get('distance')
    if distance:
        print(f"Received Distance: {distance} cm")
        return jsonify({"status": "success", "distance": distance})
    return jsonify({"status": "error", "message": "No data received"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
