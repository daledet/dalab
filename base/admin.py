from django.contrib import admin
from .models import Post, Note, Contact, Category

admin.site.register(Post)
admin.site.register(Note)
admin.site.register(Contact)
admin.site.register(Category)
