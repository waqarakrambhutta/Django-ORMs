from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count,Max,Min
from store.models import Product



def say_hello(request):
    result=Product.objects.aggregate(Min('unit_price'))
    
    return render(request, 'hello.html', {'name': 'Waqar','result':result})
    

    
    