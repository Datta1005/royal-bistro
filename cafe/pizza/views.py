from django.shortcuts import render

# Create your views here.
def PizzaInfoView(r):
    return render(r,'pizza/pizzainfo.html')