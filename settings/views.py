from unicodedata import category
from django.shortcuts import render
from . import models
from property.models import PropertyPlace, Category, Property
from blog.models import Post
from django.db.models.query_utils import Q
from django.db.models import Count
from django.contrib.auth.models import User
from django.views.generic import ListView

# Create your views here.

def home(request):
    places = PropertyPlace.objects.all().annotate(count=Count('property_place'))
    categories = Category.objects.all()
    
    hotels_list = Property.objects.filter(category__name='Hotel')[:4]
    restaurant_list = Property.objects.filter(category__name='Restaurant')[:4]
    places_list = Property.objects.filter(category__name='Places')[:4]
    
    recent_posts = Post.objects.all()[:4]
    user_count = User.objects.all().count()
    places_count = Property.objects.filter(category__name='Places').count()
    hotels_count = Property.objects.filter(category__name='Hotel').count()
    restaurant_count = Property.objects.filter(category__name='Restaurant').count()
    return render(request, 'settings/home.html',
                context={'places':places ,
                        'categories':categories,
                        'hotels_list': hotels_list,
                        'restaurant_list': restaurant_list,
                        'places_list': places_list,
                        "recent_posts":recent_posts,
                        "user_count":user_count,
                        "places_count":places_count,
                        "hotels_count":hotels_count,
                        "restaurant_count":restaurant_count,
                        })
    
def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')
    object_list = Property.objects.filter(
        Q(title__icontains=name) & Q(place__name__icontains=place)
    )
    
    return render(request, 'settings/home_search.html', context={'object_list':object_list})



def category_search(request, slug):
    category = Category.objects.get(name=slug)
    object_list = Property.objects.filter(category=category)
    return render(request, 'settings/home_search.html', context={'object_list':object_list})
    
    
class AboutView(ListView):
    model = models.Faq
    template_name = 'settings/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = models.About.objects.last()
        return context
    