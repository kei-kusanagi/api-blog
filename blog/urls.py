from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('drfCRUD_app.api.urls')),
    path('account/',include('user_app.api.urls')),

    path('api-auth', include('rest_framework.urls')),
]
