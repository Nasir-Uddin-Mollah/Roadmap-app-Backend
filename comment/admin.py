from django.contrib import admin
from . import models
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_per_page = 15


admin.site.register(models.Comment, CommentAdmin)
