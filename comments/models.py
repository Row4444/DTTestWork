from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Comment(models.Model):
    """Comments of Posts"""

    post = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, verbose_name="Comment"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Author of comment", editable=False
    )
    body = models.CharField(max_length=255, verbose_name="Comment")
    date = models.DateTimeField(auto_now_add=True)
