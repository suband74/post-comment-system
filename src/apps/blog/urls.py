from django.urls import path
from blog.views import CommentsAPIView, PostsAPIView, Com_3_APIView, StrucAPIView


urlpatterns = [
    path("postslist", PostsAPIView.as_view()),
    path("commentslist/", CommentsAPIView.as_view()),
    path("commentslist/<int:commid>", Com_3_APIView.as_view()),
    path("poststruc/<int:post>", StrucAPIView.as_view()),
]