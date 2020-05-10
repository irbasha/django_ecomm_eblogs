from django.db import models


class Author(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	description = models.TextField(max_length=200, blank=True, null=True)
	image = models.ImageField()

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	description = models.CharField(max_length=200)
	body_text = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	no_of_comments = models.IntegerField(default=0)

	def __str__(self):
		return self.title

class Comment(models.Model):
	author = models.CharField(max_length=20)
	email = models.EmailField()
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)

	def __str__(self):
		return self.author
	

class BodyText(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	heading = models.CharField(max_length=200)
	text = models.TextField()
	image = models.ImageField(null=True)
