from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source='user.username')
    replies = serializers.SerializerMethodField()

    class Meta:
        model = models.Comment
        fields = '__all__'
        read_only_fields = ['user']

    def get_replies(self, obj):
        depth = self.context.get('depth', 1)
        if depth >= 3:
            return []
        return CommentSerializer(obj.replies.all(), many=True, context={'depth': depth + 1}).data

    def validate(self, data):
        parent = data.get('parent')
        if parent:
            depth = 1
            current = parent
            while current.parent:
                depth += 1
                current = current.parent
            if depth >= 3:
                raise serializers.ValidationError(
                    "You cannot reply more than 3 levels deep.")
        return data
