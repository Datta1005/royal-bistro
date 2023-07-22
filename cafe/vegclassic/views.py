from django.shortcuts import render
from .models import ClassicInfoModel

# Create your views here.
def VegClassicView(r):
    ClassicPizza_list = ClassicInfoModel.objects.all()

    return render(r,'vegclassic/vegclassicinfo.html',{'ClassicPizza_list':ClassicPizza_list})