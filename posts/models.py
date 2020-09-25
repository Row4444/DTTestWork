from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    """News Post"""

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    title = models.CharField(max_length=64, unique=True, verbose_name="Title")
    body = models.TextField(verbose_name="Post's body")
    date_of_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Date of create"
    )
