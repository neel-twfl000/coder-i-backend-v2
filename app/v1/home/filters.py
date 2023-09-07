import django_filters
from .models import BlogPost, Category

class BlogPostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(label="Title", lookup_expr="icontains")
    category__name = django_filters.CharFilter(label="Title", lookup_expr="icontains")
    class Mata:
        model = BlogPost
        fields = {}