from django.contrib import admin
from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostDeleteView, 
    PostUpdateView,
    PostWarningView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/warning/', PostWarningView.as_view(), name='warning'),
]