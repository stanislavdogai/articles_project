from django.urls import path

from api_v2.views import ArticleCreateAPIView, ArticleDetailApiView, ArticleUpdateApiView, ArticleDeleteApiView

app_name = 'api_v2'
urlpatterns = [
    path('article/create/', ArticleCreateAPIView.as_view(), name='article_api_create'),
    path('article/<int:pk>/detail/', ArticleDetailApiView.as_view(), name='article_api_detail'),
    path('article/<int:pk>/update/', ArticleUpdateApiView.as_view(), name='article_api_update'),
    path('article/<int:pk>/delete/', ArticleDeleteApiView.as_view(), name='article_api_delete')
]