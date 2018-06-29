from django.shortcuts import render
from django.views import View

class GatewayView(View):
    template_name = "gateway.html"

    def get(self, request):
        pass
    
    def post(self, request):
        pass
