from django.contrib import admin

from news.models import News, Comment

admin.site.register(Comment)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'changed_at', 'published']
    list_filter = ['title', 'created_at', 'published_at']
