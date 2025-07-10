from rest_framework import serializers
from . import models


class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Upvote
        fields = '__all__'
