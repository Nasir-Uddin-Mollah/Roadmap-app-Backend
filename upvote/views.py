from django.shortcuts import render
from rest_framework import viewsets, pagination
from . import models, serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from roadmapItems.models import RoadmapItem
# Create your views here.


class UpvotesPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = page_size
    max_page_size = 20


class UpvoteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Upvote.objects.all()
    serializer_class = serializers.UpvoteSerializer
    pagination_class = UpvotesPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get('id')
        item_id = self.request.query_params.get('item_id')

        if id:
            queryset = queryset.filter(id=id)
        if item_id:
            queryset = queryset.filter(item_id=item_id)
        return queryset


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def toggle_upvote(request, item_id):
    user = request.user
    try:
        item = RoadmapItem.objects.get(pk=item_id)
    except RoadmapItem.DoesNotExist:
        return Response({"error": "Item not found"}, status=404)

    upvote, created = models.Upvote.objects.get_or_create(user=user, item=item)
    if not created:
        upvote.delete()
        return Response({"upvoted": False, "count": item.item_upvotes.count()})
    return Response({"upvoted": True, "count": item.item_upvotes.count()})
