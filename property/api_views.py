from .models import Property
from .serializers import PropertySerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
# from django.contrib.auth.models import User


class PropertyApiListView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    # permission_classes = [IsAdminUser]
    
    
class PropertyApiDetailView(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer