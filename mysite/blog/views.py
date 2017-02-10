from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import ArticlePost, Comment
from .forms import CommentForm

def index(request):
	post = ArticlePost.objects.filter(status='published')
	return render(request, 'blog/list.html', {'posts': post})

def article_detail(request, article_id):
	article = get_object_or_404(ArticlePost, id=article_id)
	comments = article.comments.filter(active=True)

	if request.method == 'GET':
		comment_form = CommentForm()

	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.articlepost = article
			new_comment.save()
			return HttpResponseRedirect(reverse('blog:article_detail', args=(article.id,)))

	return render(request, 'blog/detail.html', {'article':article, 'comments':comments, 'comment_form':comment_form})
