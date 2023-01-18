from django.shortcuts import render
from store.models import Product
from django.contrib.contenttypes.models import ContentType
from tags.models import Tag

def say_hello(request):
    # tag=Tag()
    # tag.label='this is first tag.'
    # tag.save()
    # tag.id

    Tag.objects.create(label='this is my second tag')
    

    return render(request, 'hello.html', {'name': 'Waqar'})

