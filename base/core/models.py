from django.db import models
from martor.models import MartorField


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_email = models.EmailField()
    author_intro = models.CharField(max_length=300)
    author_bio = models.TextField()
    author_image = models.ImageField()

    def __str__(self):
        return self.author_name


class Category(models.Model):
    blog_category = models.CharField(max_length=100)

    def __str__(self):
        return self.blog_category


class Entry(models.Model):
    blog_image = models.ImageField(null=True)
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body_text = MartorField()
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    no_of_comments = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=20)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey('Entry', on_delete=models.CASCADE)

    def __str__(self):
        return self.author
