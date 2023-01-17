from django.shortcuts import render
from store.models import Product,Customer
from django.db.models import Value,F, ExpressionWrapper,DecimalField

def say_hello(request):
    discounted_price = ExpressionWrapper(F('unit_price') * 0.8,output_field=DecimalField())
    result=Product.objects.annotate(
    discount= discounted_price 
        )
    
    return render(request, 'hello.html', {'name': 'Waqar','result':list(result)})