from django.db import models

# Create your models here.

STATUS_CHOICES = [
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed')
]


class CategoryName(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class RoadmapItem(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ForeignKey(CategoryName, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='In Progress')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
