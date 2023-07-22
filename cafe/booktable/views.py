from django.shortcuts import render
from.models import BookTableModel
from.forms import BookTableForm
from django.http import HttpResponseRedirect

# Create your views here.
def BookTableView(r):
    form = BookTableForm()
    if r.method =="POST":
        form = BookTableForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(r,'booktable/table.html',{'form':form})