from __future__ import print_function
from twilio.rest import Client

class CommunicationsPlugin(object):
    def __init__(self, account: str, token: str, from_phone: str):
        self.client = Client(account,token)
        self.from_phone = from_phone

    def send_sms(self, to_phone: str, message: str):
        status_code = 505
        try:
            message = self.client.messages.create(
                to=to_phone,
                from_=self.from_phone,
                body=message
            )
            if message:
                status_code = 202
        except Exception as e:
            print(e)
        return status_code
