from django.shortcuts import render
from store.models import Product
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem

def say_hello(request):
    queryset=TaggedItem.objects.get_tags_for(Product, 1)


    return render(request, 'hello.html', {'name': 'Waqar','tags':list(queryset)})

