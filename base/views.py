from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Note
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator


def home(request):
    return render(request, 'home.html', {})


def cv(request):
    return render(request, 'cv.html', {})


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


# class AddArticleView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'add_post.html'


# class UpdateArticleView(UpdateView):
#     model = Post
#     form_class = UpdateForm
#     template_name = 'update_post.html'
#     # fields = ['title', 'title_tag', 'body']


# class DeleteArticleView(DeleteView):
#     model = Post
#     template_name = 'delete_post.html'
#     success_url = reverse_lazy('home')
