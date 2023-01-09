from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count,Max
from store.models import Product



def say_hello(request):
    result=Product.objects.filter(unit_price__gt=1.3).aggregate(Count('unit_price'))
    
    return render(request, 'hello.html', {'name': 'Waqar','result':result})
    

    
    