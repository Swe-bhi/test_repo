from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    print("Received request at /create-payment-intent")
    data = request.get_json()
    print(f"Request data: {data}")
    amount = data.get('amount')
    print(f"Amount received: {amount}")
    response = jsonify(clientSecret=f'mock_secret_{amount}')
    print(f"Response: {response.get_json()}")
    return response

if __name__ == '__main__':
    print("Starting mock Stripe API server on port 5000...")
    app.run(host='0.0.0.0', port=5000)


