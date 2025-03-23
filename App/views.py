from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, ArticleForm
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from .models import Article, Tag, User


# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Неправильное имя пользователя или пароль')
        else:
            form.add_error(None, 'Форма не прошла проверку')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user.id
            article.save()
            form.save_m2m()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'news/create_article.html', {'form': form})



def article_list(request):
    tag = request.GET.get('tag')
    if tag:
        articles = Article.objects.filter(tags__name=tag)
    else:
        articles = Article.objects.all()
    
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'news/article_list.html', {'page_obj': page_obj, 'tag': tag, 'user': request.user})

@login_required
def edit_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'news/edit_article.html', {'form': form, 'article': article})

@login_required
def delete_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.delete()
        return render(request, 'news/delete_article.html', {'article': article})
    return render(request, 'news/confirm_delete.html', {'article': article})