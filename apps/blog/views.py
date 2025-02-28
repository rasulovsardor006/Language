from rest_framework.generics import RetrieveAPIView

from apps.blog.models import Post
from apps.blog.serializers import PostSerializer


class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# Create your views here.
