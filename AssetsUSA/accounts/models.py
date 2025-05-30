from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    # Each note belongs to a specific user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
