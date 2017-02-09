from django.shortcuts import render, get_object_or_404

from .models import ArticlePost, Comment

def index(request):
	post = ArticlePost.objects.filter(status='published')
	return render(request, 'blog/list.html', {'posts': post})
