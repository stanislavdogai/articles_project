from http import HTTPStatus

from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response

from api_v2.serializers import ArticleSerializer

from webapp.models import Article


class ArticleListApiView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

class ArticleCreateApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.CREATED)
        except ValidationError as err:
            return Response(data=err.detail, status=HTTPStatus.BAD_REQUEST)

class ArticleDetailApiView(APIView):
    def get(self, request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

class ArticleUpdateApiView(APIView):
    def put(self, request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        serializer = ArticleSerializer(data=request.data, instance=article)
        try:
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)
        except ValidationError as err:
            return Response(data=err.detail, status=HTTPStatus.BAD_REQUEST)

class ArticleDeleteApiView(APIView):
    def delete(self, request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        article.delete()
        return Response({'pk' : kwargs['pk']}, status=204)