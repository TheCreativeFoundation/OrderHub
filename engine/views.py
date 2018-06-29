from __future__ import print_function
from dotenv import load_dotenv
import os
from django.shortcuts import render, redirect
from django.views import View
from plugins.stripe_plugin import PaymentsPlugin
from plugins.twilio_plugin import CommunicationsPlugin
from plugins.transactions_plugin import TransactionsPlugin

try:
    load_dotenv()
except:
    pass

transactions_client = TransactionsPlugin(None, None, None, None)
payments_client = PaymentsPlugin(None,None)
communications_client = CommunicationsPlugin(None, None)

class OrdersView(View):
    def get(self, request):
        pass
