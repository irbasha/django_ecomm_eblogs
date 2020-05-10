from django.contrib import admin
from .models import Post, Category, Comment, Author, BodyText


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on', 'last_modified']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Author)
