from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status, parsers
# from rest_framework.response import Response
from .serializer import CategorySerializer, BlogPostSerializer,Category, BlogPost
from django.db.models import Count
from ..filters import BlogPostFilter

class CategoryViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects
    serializer_class = CategorySerializer
    http_method_names = ["get"]
    lookup_field = 'name_slug'

    def get_queryset(self):
        return self.queryset.all().annotate(total_post=Count('blog_post'))

class BlogPostViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = BlogPost.objects
    serializer_class = BlogPostSerializer
    filter_class = BlogPostFilter
    http_method_names = ["get"]
    lookup_field = 'title_slug'

    def get_filter_data(self):
        data = self.queryset.all()
        return self.filter_class(self.request.GET , data)

    def get_queryset(self):
        return self.get_filter_data().qs

