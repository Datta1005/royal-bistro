from django.shortcuts import render
from .models import VegInfoModel
# Create your views here.
def VegInfoView(r):
   Burger_list = VegInfoModel.objects.all()

   return render(r,'veg/veginfo.html',{"Burger_list":Burger_list})

