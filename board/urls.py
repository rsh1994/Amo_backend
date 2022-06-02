from django.urls import path, include
from .views import BoardViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('board', BoardViewSet, basename='board')
router.register('comment', CommentViewSet, basename='comment')

urlpatterns =[
    path('', include(router.urls))
]