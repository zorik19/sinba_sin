from rest_framework import viewsets

from .serializers import (
    BlogCategorySerializer,
    ContentPostSerializer,
    ContentPostListRetrieveSerializer,
    BlogCategoryDetailSerializer
)
from ..models import BlogCategory, ContentPost


class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

    action_to_serializer = {
       "retrieve": BlogCategoryDetailSerializer,
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class ContentPostViewSet(viewsets.ModelViewSet):
    queryset = ContentPost.objects.all()
    serializer_class = ContentPostSerializer

    action_to_serializer = {
        "list": ContentPostListRetrieveSerializer,
        "retrieve": ContentPostListRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )

# from rest_framework.views import APIView
# from rest_framework.response import Response


# class testAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         data = [{"id": 1, "name": "SBV"}, {"id": 2, "name": "Volokolamka"}]
#         return Response(data)
