from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count
from store.models import Product



def say_hello(request):
    result=Product.objects.aggregate(Count('unit_price'))
    
    return render(request, 'hello.html', {'name': 'Waqar','result':result})
    

    
    