from django.urls import path
from .views import home, home_search, category_search, AboutView

app_name = 'settings'

urlpatterns = [
    path('', home , name = 'home'),
    path('search/', home_search , name= 'home_search'),
    path('about/', AboutView.as_view() , name= 'about'),
    path('category/<slug:slug>', category_search , name= 'category_search'),
]