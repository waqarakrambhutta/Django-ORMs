from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product,Customer
from django.db.models import Value,F,Func,Count




def say_hello(request):
    result=Customer.objects.annotate(
        order_count=Count('order')
    )
    
    return render(request, 'hello.html', {'name': 'Waqar','result':list(result)})