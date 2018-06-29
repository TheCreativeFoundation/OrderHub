from __future__ import print_function
from dotenv import load_dotenv
import os
from django.shortcuts import render, redirect
from django.views import View
import sys

sys.path.append("/plugins")

from communications_plugin import CommunicationsPlugin
from transactions_plugin import TransactionsPlugin
from payments_plugin import PaymentsPlugin

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
