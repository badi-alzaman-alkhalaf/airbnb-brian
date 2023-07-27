from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.


class Property(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length =500)
    owner = models.ForeignKey(User, related_name="property_owner", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')
    place = models.ForeignKey("PropertyPlace", related_name="property_place", on_delete=models.CASCADE)
    price = models.IntegerField()
    tags = TaggableManager()
    category = models.ForeignKey('Category', related_name='property_category', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        super(Property, self).save(*args, **kwargs) 
        
        
    def get_absolute_url(self):
        return reverse('property:property_detail', kwargs={'slug': self.slug})
    
    
    def __str__(self):
        return self.title
    
    
    
class PropertyPlace(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="place/")
    
    def __str__(self):
        return self.name
    
    
class PropertyImages(models.Model):
    image = models.ImageField(upload_to='property_images/')
    property = models.ForeignKey(Property, related_name="property_images", on_delete=models.CASCADE)

    def __str__(self):
        return self.property.title
    
rate_valus = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]
class PropertyRate(models.Model):
    rate = models.IntegerField(choices=rate_valus, default=0)
    owner = models.ForeignKey(User, related_name="rate_owner", on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name="property_rates", on_delete=models.CASCADE)
    feedback = models.TextField(max_length=200, default="")
    def __str__(self):
        return self.property.title
    
    
class PropertyReservation(models.Model):
    owner = models.ForeignKey(User, related_name="reservation_owner", on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name="property_reservation", on_delete=models.CASCADE)
    date_from = models.DateField(auto_now=False, auto_now_add=False)
    date_to = models.DateField(auto_now=False, auto_now_add=False)
    guest = models.IntegerField(choices=rate_valus, default=1)
    children = models.IntegerField(choices=rate_valus, default=1)

class Category(models.Model):
    icon = models.ImageField(upload_to='category/', blank=True, null=True)
    name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name
    

