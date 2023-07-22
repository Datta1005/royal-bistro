from django.shortcuts import render
from .models import NonVegClassicModel

# Create your views here.
def NonVegClassicView(r):
    NonvegClassicPizza_list = NonVegClassicModel.objects.all()

    return render(r,'nonvegclassic/nonvegclassicinfo.html',{"NonvegClassicPizza_list":NonvegClassicPizza_list})

