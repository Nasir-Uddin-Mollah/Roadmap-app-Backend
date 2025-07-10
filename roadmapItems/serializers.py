from rest_framework import serializers
from . import models


class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryName
        fields = '__all__'


class RoadmapItemSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    upvote_count = serializers.SerializerMethodField()
    upvoted = serializers.SerializerMethodField()

    class Meta:
        model = models.RoadmapItem
        fields = ['id', 'title', 'description', 'category',
                  'status', 'created_at', 'upvote_count', 'upvoted']

    def get_upvote_count(self, obj):
        return obj.item_upvotes.count()

    def get_upvoted(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.item_upvotes.filter(user=request.user).exists()
        return False
