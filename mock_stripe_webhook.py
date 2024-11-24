from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.get_json()
    event = payload.get('type')

    if event == 'payment_intent.succeeded':
        print('Payment succeeded, triggering GitHub Actions workflow...')
        # Trigger GitHub Actions workflow
        # Read the PAT from an environment variable 
        github_token = os.getenv('PA_TOKEN')
        response = requests.post('https://api.github.com/repos/Swe-bhi/test_repo/dispatches', json={
            "event_type": "payment_success"
        }, headers={
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': f'token {github_token}'
        })
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")
        return jsonify({'status': 'Workflow triggered'}), 200
    else:
        print(f'Unhandled event type: {event}')
        return jsonify({'status': 'Unhandled event type'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)



