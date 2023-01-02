from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product,Order



def say_hello(request):
    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:10] 
    # if we write minus with the field name itmeans it is sorted in descending order.
    # or if there's not any sign than it means it is sorted in the ascending order.
    return render(request, 'hello.html', {'name': 'Waqar','products':list(queryset)})
    
# def say_hello(request):
#     queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]    
#     return render(request, 'hello.html', {'name': 'Waqar','products':list(queryset)})
    
    