from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Articles, Comments
from .serializers import CommentSerializer, ArticleSerializer


class ArticlesViewSet(ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer


class CommentsAPIView(APIView):

    article_param_config = openapi.Parameter(
        "article",
        in_=openapi.IN_QUERY,
        description="ID статьи",
        type=openapi.TYPE_INTEGER,
    )

    comment_param_config = openapi.Parameter(
        "comment",
        in_=openapi.IN_QUERY,
        description="ID комментария",
        type=openapi.TYPE_INTEGER,
    )

    depth_param_config = openapi.Parameter(
        "depth",
        in_=openapi.IN_QUERY,
        description="Уровень глубины комментариев",
        type=openapi.TYPE_INTEGER,
    )

    @swagger_auto_schema(
        manual_parameters=[
            article_param_config,
            comment_param_config,
            depth_param_config,
        ]
    )
    def get(self, request):
        if request.GET.get("depth"):
            depth = int(request.GET.get("depth"))
        else:
            depth = 0

        if request.GET.get("article"):
            node = Comments.objects.filter(article=request.GET.get("article"))
            if node and depth != 0:
                lst = (
                    node.get_descendants(include_self=True)
                    .filter(level__lte=depth - 1)
                    .values()
                )
            elif node and depth == 0:
                lst = node.get_descendants(include_self=True).values()
            post = Articles.objects.get(pk=request.GET.get("article"))

            return Response({f"{post}": list(lst)})

        elif not request.GET.get("article"):
            node = Comments.objects.filter(pk=request.GET.get("comment"))

            if node:
                if depth != 0:
                    level_node = node[0].level
                    lst = (
                        node.get_descendants(include_self=False)
                        .filter(level__lte=level_node + depth)
                        .values()
                    )
                elif depth == 0:
                    lst = node.get_descendants(include_self=False).values()
                return Response({f"{node[0].content}": list(lst)})

            else:
                return Response("Нет таких комментариев")

        else:
            return Response("Укажите статью или комментарий")

    @swagger_auto_schema(request_body=CommentSerializer)
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
