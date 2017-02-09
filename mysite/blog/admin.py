from django.contrib import admin
from .models import ArticlePost, ArticleTag

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'status', 'published')
	list_filter = ('status', 'published')
	search_fields = ('title', 'body')
	ordering = ('status', 'published')
	fieldsets = (
		(None, {'fields': ['title', 'slug', 'author', 'body', 'status']}),
		('Tag', {'fields': ['article_tag']}),
		('Date information', {'fields': ['published']})
	)		
admin.site.register(ArticlePost, ArticleAdmin)
admin.site.register(ArticleTag)
