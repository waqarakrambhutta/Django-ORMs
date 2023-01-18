from django.shortcuts import render
from store.models import Product
from django.contrib.contenttypes.models import ContentType
from store.models import Product,Collection

def say_hello(request):
    
    collection = Collection()
    collection.title= 'Video games.'
    # collection.featured_product = Product(pk=1)
    collection.featured_product_id = 1
    collection.save()
    collection.id

    # this is shorter approch but i'll not prefer it.
    # collection= Collection.objects.create(title='video game',featured_product=1)
    # collection.id

    return render(request, 'hello.html', {'name': 'Waqar'})

