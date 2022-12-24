from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from store.models import Product


def say_hello(request):
    queryset = Product.objects.filter(~Q(inventory__lt=10))

    return render(request, 'hello.html', {'name': 'Waqar','products':list(queryset)})