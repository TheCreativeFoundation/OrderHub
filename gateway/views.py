from __future__ import print_function
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
import json
import requests

class GatewayView(View):
    
    def get(self, request) -> HttpResponse:
        return render(request, "gateway.html", context=None)

    def post(self, request) -> HttpResponse:
        body: dict = json.loads(request.body.decode("utf-8"))
        # cache information here
        template_data: dict = {"cost":body["cost"]}
        return render(request, "gateway.html", template_data)