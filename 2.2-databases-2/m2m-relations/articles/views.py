from django.shortcuts import render

from .models import Article


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all().order_by('-published_at')
    context = {
        'object_list': object_list
    }
    return render(request, template, context)
