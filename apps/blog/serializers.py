from rest_framework import serializers

from sorl.thumbnail import get_thumbnail

from apps.blog.models import Post
from django.conf import settings


class PostSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'image', 'resized_image')

    def get_image(self, obj):
        image_url = get_thumbnail(obj.image, '120x120', crop='center', quality=50).url
        return f'{settings.BACKEND_URL}{image_url}'
