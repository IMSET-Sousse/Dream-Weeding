
from django.shortcuts import render
from .models import Article

def liste_articles(request):
    articles = Article.objects.all()  # ou une autre logique pour obtenir les articles
    return render(request, 'wedding/liste_articles.html', {'articles': articles})

from django.shortcuts import render, get_object_or_404

def detail_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/detail_article.html', {'article': article})