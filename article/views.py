from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Article
from .forms import ArticleForm

# Create your views here.
def list_article(request):
    articles = Article.objects.filter().order_by('date_created')
    context =  {'articles': articles}
    return render(request, 'article/list.html', context)
    
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save(commit=False)
            article.date_created = timezone.now()
            article.save()

            return redirect('/')
    else:
        form = ArticleForm()
        context = {'form' : form}
        return render(request, 'article/create.html', context)
    

def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance = article)

        if form.is_valid():
            article = form.save(commit=False)
            article.date_created = timezone.now()
            article.save()

            return redirect('/')
    else:
        form = ArticleForm(instance = article)
        context = {'form' : form}
        return render(request, 'article/edit.html', context)

def view_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'article/detail.html', context)

def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('/')