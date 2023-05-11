from blog.models import Author, Comments, Post, Tag
from django.contrib import admin

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ['author', 'tags', 'date']
    list_display = ['title', 'date', 'author']
    prepopulated_fields = {'slug': ('title', 'exerpt')}


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'post', 'user_email']


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comments, CommentsAdmin)
