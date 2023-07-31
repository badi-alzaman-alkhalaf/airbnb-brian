from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='post_detail'),
    path('category/<str:slug>', views.PostsByCategoryView.as_view(), name='posts_by_category'),
    path('tag/<str:slug>', views.PostsByTagView.as_view(), name='posts_by_tag'),
]