from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
    queryset = Product.objects.earliest('unit_price')
    

    return render(request, 'hello.html', {'name': 'Waqar','products':list(queryset)})