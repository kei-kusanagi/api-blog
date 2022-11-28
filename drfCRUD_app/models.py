from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    entrada = models.TextField()
    fecha = models.DateTimeField(auto_now=True)
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)