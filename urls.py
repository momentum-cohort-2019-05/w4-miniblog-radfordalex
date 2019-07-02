from django.urls import path, include
from . import views
from django.conf.urls import re_path
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.BlogPostListView.as_view(), name='blog'),
    path('blog/<int:pk>', views.BlogPostDetailView.as_view(), name='blog-detail'),
    path('blogger/', views.BloggerListView.as_view(), name='blogger'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('comment/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]