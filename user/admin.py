from django.contrib import admin

# Register your models here.
from .models import Post, Comment

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')

admin.site.register(Post, AuthorAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')

admin.site.register(Comment, CommentAdmin)