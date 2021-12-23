from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime, date
from django.urls import reverse

STATUS = ((0, "Draft",), (1, "Published"))

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add = True)
    content = models.TextField(blank=True)
    feature_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blogpost_likes', blank=True)
    category = models.CharField(max_length=255, default='uncategorized')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"comment {self.body} by {self.name}"


class UserPost(models.Model):
    title = models.CharField(max_length=255)
    slug = {'slug':('title',)}
    author = '{{ user.username }}'
    content = models.TextField()
    feature_image = CloudinaryField('image', default='placeholder')
    status = 'status'
    category = models.CharField(max_length=255, default='uncategorized')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
         return reverse('home')