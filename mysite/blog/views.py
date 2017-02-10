from django.shortcuts import render, get_object_or_404

from .models import ArticlePost, Comment

def index(request):
	post = ArticlePost.objects.filter(status='published')
	return render(request, 'blog/list.html', {'posts': post})

def article_detail(request, article_id):
	article = get_object_or_404(ArticlePost, id=article_id)
	comments = article.comments.filter(active=True)
	return render(request, 'blog/detail.html', {'article':article, 'comments':comments})
