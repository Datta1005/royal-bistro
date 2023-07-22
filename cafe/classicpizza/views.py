from django.shortcuts import render

# Create your views here.
def ClassicPizzaView(r):
    return render(r,'classicpizza/classicpizzainfo.html')