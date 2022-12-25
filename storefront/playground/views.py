from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
    queryset = Product.objects.values_list('id','title','collection__title')
    
    return render(request, 'hello.html', {'name': 'Waqar','products':list(queryset)})