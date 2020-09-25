from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Like(models.Model):
    """Likes of Posts"""

    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_like = models.DateField(auto_now_add=True)
