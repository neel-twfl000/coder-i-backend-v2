from rest_framework import serializers
from v1.home.models import Category, BlogPost

class CategorySerializer(serializers.ModelSerializer):
    total_post = serializers.IntegerField()
    class Meta:
        model = Category
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'