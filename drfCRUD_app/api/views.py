from django.http import JsonResponse
from rest_framework import filters, generics, status, viewsets
from rest_framework.permissions import (IsAuthenticated, IsAuthenticatedOrReadOnly)

from drfCRUD_app.models import Blog
from drfCRUD_app.api import permissions

from .serializers import BlogSerializer


class BlogVS(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class blog_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsReviewUserOrReadOnly]
    throttle_scope = 'review-detail'