from rest_framework import routers
from drfCRUD_app.api import views
from django.urls import path, include

router = routers.DefaultRouter()

router.register('api/blog', views.BlogVS, 'blog')

urlpatterns = [
    path('blogreview/<int:pk>/', views.blog_detail.as_view(), name='blog_detail'),
] + router.urls