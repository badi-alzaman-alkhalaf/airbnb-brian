from django.urls import path
from . import views
from .api_views import post_list_api, post_detail_api

app_name = 'blog'


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='post_detail'),
    path('category/<str:slug>', views.PostsByCategoryView.as_view(), name='posts_by_category'),
    path('tag/<str:slug>', views.PostsByTagView.as_view(), name='posts_by_tag'),
    
    
    
    # api
    path('api/list', post_list_api, name='post_list_api'),
    path('api/<int:id>', post_detail_api, name='post_detail_api'),
    
    
]