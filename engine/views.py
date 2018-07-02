from __future__ import print_function
from dotenv import load_dotenv
import os
import json
import hashlib
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from . import communications_plugin, logistics_plugin, payments_plugin

try:
    load_dotenv()
except:
    pass

logistics_client = logistics_plugin.LogisticsPlugin(None, None, "payhub-transactions", "us-east-2")
communications_client = communications_plugin.CommunicationsPlugin(None, None, None)
payments_client = payments_plugin.PaymentsPlugin(None)

def index(request,):
    return "Hello from the index"

class SendOrderView(View):
    failed_template = "failedSendOrder.html"
    success_template = "successSendOrder.html"

    def post(self, request) -> HttpResponse:
        status_code: int = 505
        status_code = logistics_client.record_transaction(request.POST)
        if status_code == 202:
            description: str = "Order of: {} for {} through the PayHub Gateway".format(request.POST["cost"],request.POST["order"])
            status_code = payments_client.charge_customer(request.POST["cost"], description, request.POST.get("stripe_token"))
            if status_code = 202:
                # send order to business through adding the order with appsync and dynamodb

                return render(request, self.success_template, context=None)
        return render(request, self.failed_template, {"status_code":status_code})

class CompleteOrderView(View):
    def post(self, request) -> HttpResponse:
        status_code: int = 505
        response_body: dict = {"message":"An error occured!"}
        body: dict = json.loads(request.body.decode("utf-8"))
        message: str = "Hey youre order is complete"  # make this better
        status_code_1: int = communications_client.send_sms(body["to_phone"],message)
        if status_code_1 == 202:
            status_code = 202
        return HttpResponse({"statusCode":status_code,"body":response_body})

class SendOrderSuccessView(View):
    template_name = "sendOrderSuccess.html"

    def get(self, request) -> HttpResponse:
        return render(request, self.template_name, context=None)

class SendOrderFailedView(View):
    template_name = "sendOrderFailed.html"

    def get(self, request) -> HttpResponse:
        return render(request, self.template_name, context=None)
