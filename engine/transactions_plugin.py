from __future__ import print_function
from boto3.session import Session
import hashlib
import datetime

class TransactionsPlugin(object):
    def __init__(
        self, aws_access_key: str, aws_access_secret: str, table_name: str, region: str
    ):
        self.client = Session(
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_access_secret,
            region_name=region,
        )
        self.transactions_table = self.client.resource("dynamodb").Table(table_name)

    def record_transaction(self, transaction_body: dict):
        status_code = 505
        current_datetime = str(datetime.datetime.now())
        transaction_id = hashlib.sha256(
            str(transaction_body["customer"] + current_datetime)
        ).hexdigest()
        try:
            response = self.transactions_table.put_item(
                Item={
                    "transaction_id": transaction_id,
                    "order": transaction_body["order"],
                    "cost": transaction_body["cost"],
                    "business_id": transaction_body["business_id"],
                    "customer": transaction_body["customer"],
                    "datetime": current_datetime,
                }
            )
            if response:
                status_code = 202
        except Exception as e:
            print(e)
        return status_code
