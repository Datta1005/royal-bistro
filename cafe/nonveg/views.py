from django.shortcuts import render
from .models import NonVegInfoModel
# Create your views here.
def NonVegInfoView(r):
   Burger_list = NonVegInfoModel.objects.all()

   return render(r,'nonveg/nonveginfo.html',{"Burger_list":Burger_list})

