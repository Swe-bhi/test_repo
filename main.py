from stripe_adapter import StripeAdapter
from aws_adapter import AWS_EC2_Adapter

def main():
    stripe = StripeAdapter()
    aws_ec2 = AWS_EC2_Adapter()

    # Step 1: Pay to Stripe
    client_secret = stripe.create_payment_intent(100)
    print(f'Payment successful, client secret: {client_secret}')

    # Step 2: Connect to "adapter" AWS EC2 API
    vm_id = aws_ec2.create_vm('testVM')
    print(f'VM created, ID: {vm_id}')

    # Step 3: Run VM and get message
    message = aws_ec2.run_vm(vm_id)
    print(f'VM Message: {message}')

if __name__ == "__main__":
    main()

