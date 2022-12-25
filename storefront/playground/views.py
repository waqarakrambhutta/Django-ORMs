from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Customer


def say_hello(request):
    queryset = Customer.objects.earliest('last_name')
    

    return render(request, 'hello.html', {'name': 'Waqar','products':list(queryset)})
    
    
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.db.models import Q, F
# from store.models import Product


# def say_hello(request):
#     queryset = Product.objects.filter(customer__startswith='F')
    

#     return render(request, 'hello.html', {'name': 'Waqar','products':list(queryset)})