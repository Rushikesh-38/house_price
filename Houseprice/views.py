from django.shortcuts import render
from .forms import Queryform
from django.http import HttpResponse
# Create your views here.
def show(r):
    form = Queryform()
    my_dict = {'form': form}
    if r.method == 'POST':
        form = Queryform(r.POST)
        if form.is_valid():
            form.save(commit=True)
        return HttpResponse('<h1>Thank you!</h1>')
    return render(r,'houseprice.html',my_dict)
