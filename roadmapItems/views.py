from django.shortcuts import render
from rest_framework import viewsets, filters, pagination
from . import models, serializers
# Create your views here.


class CategoryNameViewSet(viewsets.ModelViewSet):
    queryset = models.CategoryName.objects.all()
    serializer_class = serializers.CategoryNameSerializer


class RoadmapItemPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = page_size
    max_page_size = 20


class RoadmapItemViewSet(viewsets.ModelViewSet):
    queryset = models.RoadmapItem.objects.all()
    serializer_class = serializers.RoadmapItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name', 'status']
    pagination_class = RoadmapItemPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get('id')

        if id:
            queryset = queryset.filter(id=id)
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context