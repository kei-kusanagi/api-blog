from rest_framework import serializers
from drfCRUD_app import models

class BlogSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = models.Blog
        # fields = ('id', 'titulo', 'entrada', 'fecha', 'review_user',)
        fields = "__all__"
        read_only_fields = ('fecha','review_user',)
        