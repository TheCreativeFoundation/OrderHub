from __future__ import print_function
import stripe

class PaymentsPlugin(object):
    def __init__(self, stripe_api_key: str):
        self.stripe_client = stripe.api_key
        self.stripe_api_key = stripe_api_key

    def charge_customer(self, cost: int, description: str, stripe_token) -> int:
        status_code = 505
        currency = "usd"
        if stripe_token != None:
            try:
                charge = stripe.Charge.create(
                    amount=cost,
                    currency=currency,
                    description=description,
                    source=stripe_token
                )
                if charge:
                    status_code = 202
            except stripe.error.CardError as e:
                print(e)
                status_code = 415 # CARD DECLINED ERROR
            except stripe.error.APIConnectionError as e:
                print(e)
                status_code = 416 # NETWORK ERROR
            except stripe.error.AuthenticationError as e:
                print(e)
                status_code = 417 # AUTH ERROR
            except Exception as e:
                print(e)
        else:
            status_code = 408 # MISSING STRIPE TOKEN FOR PAYMENT
        return status_code