from django.urls import path

from . import views
from .views import BlogHomeView, PostDetailsView, UserPostsView, CreatePostView,EditPostView, DeletePostView
urlpatterns = [
    #path('homeblog/', views.blog_home, name='home-blog')
    path('bloghome/', BlogHomeView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailsView.as_view(), name='post-details'),
    path('posts/', UserPostsView.as_view(), name='user-posts'),
    path('createPost/', CreatePostView.as_view(), name='create-post'),
    path('editPost/<int:pk>', EditPostView.as_view(), name='edit-post'),
    path('deletePost/<int:pk>', DeletePostView.as_view(), name='delete-post')

]
