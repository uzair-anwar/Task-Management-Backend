from django.urls import path, include
from rest_framework import routers
from .views import CommentViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'', TaskViewSet, basename="tasks")
router.register(r'(?P<task_id>\d+)/comments',
                CommentViewSet, basename="comments")
urlpatterns = [
    path('', include(router.urls)),
]
