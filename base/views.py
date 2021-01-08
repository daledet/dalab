from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Note, Category
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html', {})


def cv(request):
    return render(request, 'cv.html', {})


def data(request):
    import json
    import requests

    api_request = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?id=3137115&appid=4fbcfd9147ff6df0e3ee3de039a4e70c&units=metric")
    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error..."

    return render(request, 'data.html', {'api': api})


def projects(request):
    return render(request, 'projects.html', {})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats, 'category_posts': category_posts})


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # send an email
        send_mail(
            name,
            message,
            email,
            ['dwightledet@protonmail.com']
        )

        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})


class ArticleListView(ListView):
    paginate_by = 5
    model = Post
    template_name = 'articles.html'
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article.html'


class NoteListView(ListView):
    paginate_by = 5
    model = Note
    template_name = 'notes.html'
    ordering = ['-note_date']


class NoteDetailView(DetailView):
    model = Note
    template_name = 'note.html'
