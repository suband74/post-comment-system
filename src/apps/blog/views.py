# from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment, Posts
from .serializers import CommentSerializer, PostSerializer


class CommentsAPIView(APIView):
    def get(self, request):
        article = request.GET.get(
            "post",
        )
        lst = Comment.objects.filter(post=article, level__lte=3).values()
        # lst = list(Comment.objects.all().values())
        return Response({"post": list(lst)})

    def post(self, request):
        serializer = CommentSerializer(data=request.data)

        key_post = request.data["post"]
        if Comment.objects.filter(post=key_post).exists() is False:
            request.data["level"] = 1
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"post": serializer.data})

        else:
            key = request.data["id_kor"]
            request.data["level"] = Comment.objects.get(pk=key).level + 1
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({"post": serializer.data})


class PostsAPIView(APIView):
    def get(self, request):
        lst = Posts.objects.all().values()
        return Response({"post": list(lst)})

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


class Com_3_APIView(APIView):
    def struc(lst):
        structure = {}
        for item in lst:
            if (
                item["id_kor"] == 0
                and ("Статья" + str(item["post_id"])) not in structure
            ):
                structure.update(
                    {"Статья" + str(item["post_id"]): [item["id"]]}
                )
            elif item["id_kor"] == 0 and ("Статья" + str(item["post_id"])) in structure:
                structure["Статья" + str(item["post_id"])].append(item["id"])
            else:
                if item["id_kor"] not in structure:
                    structure.update({item["id_kor"]: [item["id"]]})
                else:
                    structure[item["id_kor"]].append(item["id"])
        return structure

    @staticmethod
    def dfs(graph, start, visited=None):
        if visited is None:
            visited = {}
            visited.update({start: {}})

        for node in graph[start]:
            if node in graph:
                visited[start].update({node: {}})
                Com_3_APIView.dfs(graph, node, visited[start])
            else:
                visited[start].update({node: None})
        return visited

    def get(self, request, commid):
        lev = Comment.objects.get(pk=commid).level
        if lev != 3:
            return Response(
                "Список комментов возможен только для статей 3 уровня"
            )
        else:
            lst = Comment.objects.all().values()
            workpiece = Com_3_APIView.struc(lst)
            structure = Com_3_APIView.dfs(workpiece, commid)
            return Response(structure)


class StrucAPIView(APIView):
    def get(self, request, post):
        lst = Comment.objects.filter(post=post).values()
        workpiece = Com_3_APIView.struc(lst)
        structure = Com_3_APIView.dfs(workpiece, "Статья" + str(post))
        return Response(structure)
