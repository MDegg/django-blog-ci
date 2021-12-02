from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on', 'category')
    search_fields = ['title','content','category']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status','created_on','category')
    summernote_fields = ('content')

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on','approved')
    list_filter = ('approved','created_on',)
    search_fields = ('name','email','body','category')
    actions = ['approve_comments']

    def approve_comments(self,request,queryset):
        queryset.update(approved=True)

# Register your models here.
