from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()

router.register(r"category", views.CategoryViewSet, basename="category")
router.register(r"post", views.BlogPostViewSet, basename="blog_post")

urlpatterns = [
    path('', include(router.urls))
]