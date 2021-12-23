from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from .views import AddPostView


urlpatterns = [
    
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('add_post/', views.AddPostView.as_view(), name = 'add_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    
]