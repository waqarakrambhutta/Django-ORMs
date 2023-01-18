from django.shortcuts import render
from store.models import Product
from django.contrib.contenttypes.models import ContentType
from store.models import Product,Collection

def say_hello(request):

    # collection = Collection.objects.get(pk=11)
    # collection.featured_product=None
    # collection.save()
    # collection.id

    Collection.objects.filter(pk=11).update(featured_product=None)
    
    return render(request, 'hello.html', {'name': 'Waqar'})

