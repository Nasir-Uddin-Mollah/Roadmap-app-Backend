from django.db import models
from django.contrib.auth.models import User
from roadmapItems.models import RoadmapItem
# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    item = models.ForeignKey(RoadmapItem, on_delete=models.CASCADE)
    body = models.TextField()
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name="replies", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} comment on {self.item.title}"
