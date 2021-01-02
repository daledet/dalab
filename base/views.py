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
    ordering = ['-post_date']


# class AddCategoryView(CreateView):
#     model = Category
#     template_name = 'add_category.html'
#     fields = '__all__'


# class UpdateArticleView(UpdateView):
#     model = Post
#     form_class = UpdateForm
#     template_name = 'update_post.html'
#     # fields = ['title', 'title_tag', 'body']


# class DeleteArticleView(DeleteView):
#     model = Post
#     template_name = 'delete_post.html'
#     success_url = reverse_lazy('home')
