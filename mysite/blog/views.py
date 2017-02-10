from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import ArticlePost, Comment
from .forms import CommentForm

def index(request):
	post = ArticlePost.objects.filter(status='published')
	paginator = Paginator(post, 15)  #每页15个标题
	
	page = request.GET.get('page')
	try:
		current_page = paginator.page(page)
		post = current_page.object_list
	except PageNotAnInteger:
		current_page = paginator.page(1)
		post = current_page.object_list
	except EmptyPage:
		current_page = paginator.page(paginator.num_pages)
		post = current_page.object_list
	return render(request, 'blog/list.html', {'posts': post, 'page':current_page})

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
