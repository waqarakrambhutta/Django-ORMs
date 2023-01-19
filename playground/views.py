from django.shortcuts import render
from store.models import Product
from django.contrib.contenttypes.models import ContentType
from store.models import Collection

def say_hello(request):

    # collection = Collection(pk=11)
    # collection.delete()

    Collection.objects.filter(pk__range=(14,24)).delete()

    return render(request, 'hello.html', {'name': 'Waqar'})

