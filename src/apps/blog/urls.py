from django.urls import path, include
from rest_framework import routers
from .views import CommentsAPIView, ArticlesViewSet


router = routers.SimpleRouter()
router.register(r'articles', ArticlesViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("comments/", CommentsAPIView.as_view()),
]
