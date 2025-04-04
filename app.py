from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Function to check wallet address
def check_wallet(wallet_address):
    url = f"https://api.cryptoscamdb.org/v1/check/{wallet_address}"
    response = requests.get(url)
    return response.json()

@app.route('/check', methods=['GET'])
def check():
    wallet = request.args.get('wallet')
    if not wallet:
        return jsonify({"error": "Enter a wallet address"}), 400
    data = check_wallet(wallet)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)