from django.shortcuts import render
from .models import Article, Author
# Create your views here.


def frontend(request):
    articles = Article.objects.order_by('-timestamp')
    authors = Author.objects.all()

    data = {
        'articles': articles,
        'authors': authors,
    }
    return render(request, 'vue_app/template.html', data)