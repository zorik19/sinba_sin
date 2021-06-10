from django.urls import path

from rest_framework import routers
from .views import BlogCategoryViewSet, ContentPostViewSet

router = routers.SimpleRouter()
router.register('category', BlogCategoryViewSet, basename='category')
router.register('content', ContentPostViewSet, basename='content')

urlpatterns = []
urlpatterns += router.urls
