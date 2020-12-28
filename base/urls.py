from django.urls import path
from . import views
from .views import ArticleListView, ArticleDetailView, NoteListView

urlpatterns = [
    path('', views.home, name="home"),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
    path('notes/', NoteListView.as_view(), name='notes'),
    path('cv/', views.cv, name="cv"),
    path('contact/', views.contact, name="contact"),
]
