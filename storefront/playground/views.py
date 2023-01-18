from django.shortcuts import render
from store.models import Product
from django.contrib.contenttypes.models import ContentType


def say_hello(request):
    
    queryset=Product.objects.all()
    queryset[0]
    list(queryset)
    
    return render(request, 'hello.html', {'name': 'Waqar'})

