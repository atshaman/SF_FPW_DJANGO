from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {'created_at': ['lt'], 'title': ['icontains'], 'author': ['exact']}
