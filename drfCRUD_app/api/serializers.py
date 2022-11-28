from rest_framework import serializers
from drfCRUD_app import models

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = ('id', 'titulo', 'entrada', 'fecha')
        read_only_fields = ('fecha',)
        review_user = serializers.StringRelatedField(read_only=True)