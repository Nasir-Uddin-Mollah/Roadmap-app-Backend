from django.db import models
from django.contrib.auth.models import User
from roadmapItems.models import RoadmapItem


class Upvote(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="upvotes")
    item = models.ForeignKey(
        RoadmapItem, on_delete=models.CASCADE, related_name="item_upvotes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'item')

    def __str__(self):
        return f"{self.user.username} upvoted {self.item.title}"
