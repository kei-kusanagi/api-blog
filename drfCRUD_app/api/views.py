from django.http import JsonResponse
from rest_framework import filters, generics, status, viewsets
from rest_framework.permissions import (IsAuthenticated, IsAuthenticatedOrReadOnly)

from drfCRUD_app.models import Blog
from drfCRUD_app.api import permissions

from .serializers import BlogSerializer
from . import permissions

class BlogVS(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.all()

    def perform_create(self, serializer):

        review_user = self.request.user
        # review_queryset = Blog.objects.filter(review_user=review_user)

        serializer.save(review_user=review_user)


class blog_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsReviewUserOrReadOnly]
    throttle_scope = 'review-detail'