# trigger_payment.py
from stripe_adapter import StripeAdapter

stripe_adapter = StripeAdapter()
client_secret = stripe_adapter.create_payment_intent(amount=1000)

