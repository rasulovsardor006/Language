from django.urls import path

from apps.blog.views import PostDetail

urlpatterns = [
    path('PostDetail/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]
