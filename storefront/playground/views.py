from django.shortcuts import render
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from store.models import Product

def say_hello(request):
   
   result = Product.objects.all().order_by('-pk')[:10]

   return render(request, 'hello.html', {'name': 'Waqar','result':list(result)})