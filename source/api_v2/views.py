from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response

from api_v2.serializers import ArticleSerializer

from webapp.models import Article


class ArticleCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        # print(request.data)
        if serializer.is_valid():
            article = serializer.save()
            print('article', article)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class ArticleDetailApiView(APIView):
    def get(self, request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

class ArticleUpdateApiView(APIView):
    def put(self, request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        serializer = ArticleSerializer(data=request.data, instance=article)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class ArticleDeleteApiView(APIView):
    def delete(self, request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        article.delete()
        return HttpResponseRedirect(reverse('webapp:index'))