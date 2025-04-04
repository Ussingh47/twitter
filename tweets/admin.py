from django.contrib import admin
from .models import Tweet, Comment, Like

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'date_posted')
    list_filter = ('date_posted', 'author')
    search_fields = ('content', 'author__username')
    date_hierarchy = 'date_posted'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'tweet', 'date_posted')
    list_filter = ('date_posted', 'author')
    search_fields = ('content', 'author__username')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'tweet', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)
