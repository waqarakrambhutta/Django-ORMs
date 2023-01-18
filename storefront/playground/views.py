from django.shortcuts import render
from store.models import Product
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem

def say_hello(request):
    content_type=ContentType.objects.get_for_model(Product)
    queryset = TaggedItem.objects \
    .select_related('tag') \
    .filter(
        content_type=content_type,
        object_id=1
    )
    return render(request, 'hello.html', {'name': 'Waqar','tags':list(queryset)})

