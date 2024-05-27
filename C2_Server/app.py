from flask import Flask, request, jsonify

app = Flask(__name__)

# Stockage des informations des bots
bots_data = []

@app.route('/register', methods=['POST'])
def register_bot():
    data = request.get_json()
    bots_data.append(data)
    return jsonify({"message": "Bot registered successfully!"}), 200

@app.route('/command', methods=['POST'])
def send_command():
    command = request.get_json()
    # Logique pour envoyer des commandes spécifiques aux bots
    return jsonify({"message": "Command sent!"}), 200

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(bots_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
