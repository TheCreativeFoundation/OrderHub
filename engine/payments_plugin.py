from __future__ import print_function
import stripe

class PaymentsPlugin(object):
    def __init__(self, stripe_api_key: str):
        stripe.api_key = stripe_api_key
        self.stripe_api_key = stripe_api_key

    def create_payment(self, payment_info: dict, order_info: dict):
        status_code = 505
        try:
            pass
        except Exception as e:
            print(e)
        return status_code
