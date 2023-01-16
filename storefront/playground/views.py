from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count,Max
from store.models import Product,Customer
from django.db.models import Value,F,Func
from django.db.models.functions import Concat



def say_hello(request):
    result=Customer.objects.annotate(
        Concat=('first_name',Value(' '),'last_name')
    )
    
    return render(request, 'hello.html', {'name': 'Waqar','result':list(result)})