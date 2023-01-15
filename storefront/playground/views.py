from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count,Max
from store.models import Product
from django.db.models import Value,F



def say_hello(request):
    result=Product.objects.annotate(tax=F('unit_price')+3)
    
    return render(request, 'hello.html', {'name': 'Waqar','result':list(result)})