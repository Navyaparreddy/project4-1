from django.shortcuts import render
from django.views import View
from django .http import HttpResponse
from .models import Product

class HomeView(View):
    def get(self,request):
        return render(request,template_name='Home.html')
class InsertInput(View):
    def get(self,request):
        return render(request,template_name='Productinput.html')
class InsertView(View):
    def get(self,request):
        P_id = int(request.GET["t1"])
        P_name = request.GET["t2"]
        P_cost = float(request.GET["t3"])
        P_mfdt = request.GET["t4"]
        P_expdt = request.GET["t5"]
        p1=Product(Pid=P_id,pname=P_name,pcost=P_cost,pmfdt=P_mfdt,pexpdt=P_expdt)
        p1.save()
        resp=HttpResponse("Product inserted Sucessfully")
        return resp
