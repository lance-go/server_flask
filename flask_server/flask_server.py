from flask import Flask, request, jsonify
import stripe
from flask_server.constant_vars import endpoint_secret, stripe_keys

app = Flask(__name__)

stripe.api_key = stripe_keys["secret_key"]

@app.route("/stripe-checkout", methods=["POST"])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    print(payload)
    id = request.args.get('id')
    print(id)
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

    except ValueError as e:
        # Invalid payload
        return "Invalid payload", 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return "Invalid signature", 400

    # Handle the payment_intent.succeeded event
    if event["type"] == "charge.succeeded":
        print("Payment was successful.")
        # TODO: run some custom code here

    return "Success", 200
