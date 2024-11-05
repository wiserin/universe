from django.shortcuts import render
from django.http import *
from .forms import ArticleForm
from .models import Articles
from django.views.generic import DetailView
from tinymce.models import HTMLField


def main_page(request):
    articles = Articles.objects.all()
    render_a = []
    for article in articles:
        id = article.id
        heading = article.heading
        dict_ = {
            'id': id,
            'heading': heading,
            'link': f'article/?id={id}'
        }
        render_a.append(dict_)
    render_a.reverse()

    return render(request, 'firstapp/main.html', {'articles': render_a})


def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponsePermanentRedirect('/')
    else:
        form = ArticleForm()

    return render(request, 'firstapp/new_article.html', {'form': form})

def article(request):
    id = request.GET.get('id', '')
    article = Articles.objects.get(id=id)
    return render(request, 'firstapp/article.html', {'article': article})

def error(request):
    return HttpResponse('Что то не так)')

