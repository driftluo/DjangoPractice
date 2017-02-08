from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ArticlePost(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	author = models.ForeignKey(User, related_name='article')
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	published = models.DateTimeField(default=timezone.now())
	status = models.CharField(max_length=10, choices=(('draft', '草稿'), ('published','发布')), default='draft')
	article_tag = models.ManyToManyField(ArticleTag, related_name='article_tag', blank=True)

	class Meta:
		ordering = ('-published',)

	def __str__(self):
		return self.title

class ArticleTag(models.Model):
	tag = models.CharField(max_length=500)

	def __str__(self):
		return self.tag

class Comment(models.Model):
	articlepost = models.ForeignKey(ArticlePost, related_name='comments', on_delete=models.CASCADE)
	name = models.CharField(max_length=80)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updatee = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering=('created',)

	def __str__(self):
		return 'Comment by {0} on {1}'.format(self.name, self.articlepost)
