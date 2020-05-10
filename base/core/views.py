from django.shortcuts import render
from .models import Post, Category, Comment
from .forms import CommentForm



def home(request):
	blogs = Post.objects.all()
	return render(request, 'index.html', {'blogs': blogs})


def category(request, category):
	blogs = Post.objects.filter(categories__name__contains=category)
	return render(request, 'index.html', {'blogs': blogs})


def detail(request, pk):
	blog = Post.objects.get(pk=pk)
	print(blog.author.name)
	form = CommentForm()
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(
				author=form.cleaned_data["author"],
				email=form.cleaned_data["email"],
                body=form.cleaned_data["body"],
                post=blog
            )
			comment.save()
			blog.no_of_comments += 1
			blog.save()
	comments = Comment.objects.filter(post=blog)
	return render(request, 'detail.html', {'blog': blog, 'comments':comments, 'form': form})


def contact(request):
    context = {}
    return render(request, "contact.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)

