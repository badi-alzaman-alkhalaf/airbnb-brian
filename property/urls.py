from django.urls import path
from . import views
from .api_views import PropertyApiListView, PropertyApiDetailView
app_name = 'property'
urlpatterns = [
    path('', views.PropertyListView.as_view(), name="property_list" ),
    path('<slug:slug>/', views.PropertyDetailView.as_view(), name="property_detail" ),
    
    
    
    # apis
    path('api/list/', PropertyApiListView.as_view(), name="property_list_api" ),
    path('api/<int:pk>/', PropertyApiDetailView.as_view(), name="property_detail_api" ),
]
