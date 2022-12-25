from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
    queryset = Product.objects.filter(id=F('orderitem__product_id')).order_by('title').distinct()
    
    return render(request, 'hello.html', {'name': 'Waqar','products':list(queryset)})