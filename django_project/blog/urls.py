
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='HomePage'),
    path('user/<str:username>', UserPostListView.as_view(), name='UserPosts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='PostDetail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='PostUpdate'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='PostDelete'),
    path('post/new/', PostCreateView.as_view(), name='PostCreate'),
]
