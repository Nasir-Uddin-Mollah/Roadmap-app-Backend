from django.contrib import admin
from . import models
# Register your models here.


class CategoryNameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.CategoryName, CategoryNameAdmin)


class RoadmapItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    search_fields = ['title', 'category', 'status']


admin.site.register(models.RoadmapItem, RoadmapItemAdmin)
