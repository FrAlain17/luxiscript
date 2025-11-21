import stripe
import paypalrestsdk
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

paypalrestsdk.configure({
  "mode": settings.PAYPAL_MODE, # sandbox or live
  "client_id": settings.PAYPAL_CLIENT_ID,
  "client_secret": settings.PAYPAL_CLIENT_SECRET 
})

def create_stripe_checkout_session(user, price_id):
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price_id,
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=settings.DOMAIN_URL + '/dashboard/billing?success=true&session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.DOMAIN_URL + '/dashboard/billing?canceled=true',
            customer_email=user.email,
        )
        return checkout_session.url
    except Exception as e:
        print(f"Stripe Error: {e}")
        return None

def create_paypal_payment(price, return_url, cancel_url):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": return_url,
            "cancel_url": cancel_url
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "Subscription",
                    "sku": "subscription",
                    "price": str(price),
                    "currency": "USD",
                    "quantity": 1
                }]
            },
            "amount": {
                "total": str(price),
                "currency": "USD"
            },
            "description": "Subscription payment"
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                return link.href
    else:
        print(payment.error)
        return None
