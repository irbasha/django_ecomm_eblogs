from django.db import models
from django.contrib import admin
from .models import Entry, Category, Comment, Author
from martor.widgets import AdminMartorWidget


class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'mod_date']
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Author)
