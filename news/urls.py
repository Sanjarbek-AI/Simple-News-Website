from django.urls import path

from news.views import NewsListView, NewsDetailView

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='list'),
    path('category/<int:pk>', NewsListView.as_view(), name='category'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='detail')
]