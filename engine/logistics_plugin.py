from __future__ import print_function
from boto3.session import Session
import hashlib
import datetime

class LogisticssPlugin(object):
    def __init__(
        self, aws_access_key: str, aws_access_secret: str, table_name: str, region: str
    ):
        self.client = Session(
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_access_secret,
            region_name=region,
        )
        self.transactions_table = self.client.resource("dynamodb").Table(table_name)

    def record_transaction(self, transaction_body) -> int:
        status_code = 505 # CRITICAL/UNKOWN ERROR
        current_datetime = str(datetime.datetime.now())
        transaction_id = hashlib.sha256(
            str(transaction_body["customer_email"] + current_datetime)
        ).hexdigest()
        try:
            response = self.transactions_table.put_item(
                Item={
                    "transaction_id": transaction_id,
                    "order": transaction_body["order"],
                    "cost": transaction_body["cost"],
                    "business_id": transaction_body["business_id"],
                    "customer": {
                        "name" : transaction_body["customer_name"],
                        "email" : transaction_body["customer_email"],
                        "phone" : transaction_body["customer_phone"]
                    },
                    "datetime": current_datetime,
                }
            )
            if response:
                status_code = 202 # SUCCESS
        except KeyError as e:
            print(e)
            status_code = 403 # DATA MISSING
        except Exception as e:
            print(e)
        return status_code

    def create_order(self) -> int:
        return 0
