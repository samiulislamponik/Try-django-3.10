from django.contrib import admin
from article.models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


admin.site.register(Article, ArticleAdmin)
