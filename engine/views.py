from __future__ import print_function
from dotenv import load_dotenv
import os
from django.shortcuts import render, redirect
from django.views import View
import sys

sys.path.append("/plugins")

from plugins import communications_plugin, payments_plugin, transactions_plugin

try:
    load_dotenv()
except:
    pass

transactions_client = transactions_plugin.TransactionsPlugin(None, None, None, None)
payments_client = payments_plugin.PaymentsPlugin(None,None)
communications_client = communications_plugin.CommunicationsPlugin(None, None)

class OrdersView(View):
    def get(self, request):
        pass
