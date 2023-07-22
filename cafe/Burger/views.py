from django.shortcuts import render

def BurgerInfoView(r):
    return render(r,'burger/burgerinfo.html')
