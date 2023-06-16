from django.contrib import admin
from .models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Article, ArticleAdmin)