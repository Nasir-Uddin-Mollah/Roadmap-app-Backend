from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('list', views.UpvoteViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('toggle-upvote/<int:item_id>/',
         views.toggle_upvote, name='toggle-upvote'),
]
