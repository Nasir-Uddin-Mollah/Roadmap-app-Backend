from django.shortcuts import render
from rest_framework import viewsets, pagination
from . import models, serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
# Create your views here.


class CommentPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = page_size
    max_page_size = 20


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    pagination_class = CommentPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get('id')
        item_id = self.request.query_params.get('item_id')

        if id:
            return queryset.filter(id=id)

        if self.action == 'list':
            if item_id:
                queryset = queryset.filter(item_id=item_id, parent=None)
            else:
                queryset = queryset.filter(parent=None)
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['depth'] = 1
        return context

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
