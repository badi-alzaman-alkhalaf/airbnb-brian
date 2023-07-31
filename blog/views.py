from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models
# Create your views here.
from django.db.models import Count
from taggit.models import Tag
from django.db.models.query_utils import Q



class PostListView(ListView):
    model = models.Post
    paginate_by = 1
    
    
    def get_queryset(self):
        name = self.request.GET.get('q', '')
        return models.Post.objects.filter(
            Q(title__icontains = name) |
            Q(description__icontains = name)
        )
    
    
class PostDetailView(DetailView):
    model = models.Post
    
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all().annotate(post_count=Count('post_category'))
        context['tags'] = Tag.objects.all()
        context['recent_posts'] = models.Post.objects.all()[:4]
        
        return context
    
class PostsByCategoryView(ListView):
    model = models.Post
    
    def get_queryset(self):
        return models.Post.objects.filter(
            Q(categories__name__icontains=self.kwargs['slug'])
        )
    

class PostsByTagView(ListView):
    model = models.Post
    
    def get_queryset(self):
        return models.Post.objects.filter(
            Q(tags__name__icontains=self.kwargs['slug'])
        )