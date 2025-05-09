from django.urls import path
from .views import (HomePageView, ArticleList, ArticleDetail, ArticleCategoryList)

urlpatterns = [
    path(r'', HomePageView.as_view(), name='home'),
    path(r'articles', ArticleList.as_view(), name='articles-list'),
    path(r'articles/category/<slug>', ArticleCategoryList.as_view(), name='articles-categories-list'),
    path(r'articles/<year>/<month>/<day>/<slug>', ArticleDetail.as_view(), name='news-detail'),
]
