from django.contrib import admin

from blog.models import Category, Post, Comment, Like, PostView

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Like)
