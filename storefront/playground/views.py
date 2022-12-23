from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    queryset = Product.objects.filter(description__)

    return render(request, 'hello.html', {'name': 'Waqar','products':list(queryset)})
