import requests

WEBHOOK_URL = "http://localhost:5002/webhook"

class StripeAdapter:
    def create_payment_intent(self, amount):
        response = requests.post(
            'http://localhost:5000/create-payment-intent',
            json={'amount': amount}
        )
        client_secret = response.json().get('clientSecret')
        
        # Trigger webhook manually for testing
        self.trigger_webhook('payment_intent.succeeded')
        
        return client_secret

    def trigger_webhook(self, event_type):
        payload = {
            'type': event_type
        }
        response = requests.post(
            WEBHOOK_URL,
            json=payload,
            headers={'Content-Type': 'application/json'}
        )
        print(f'Webhook triggered with status code: {response.status_code}')
        print(f'Webhook response: {response.text}')


