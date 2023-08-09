from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils import timezone
# Create your models here.

class Property(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length = 2000)
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
    
    def avg_rate(self): 
        rates = self.property_rates.all() # type: ignore
        rating = sum(rate.rate for rate in rates)
        return rating/len(rates) if rating > 0 else 0
    
    def check_availability(self):
        books = self.property_reservation.all() # type: ignore
        now = timezone.now().date() # type: ignore
        for book in books:
            if now < book.date_from and  now > book.date_to:
                return "available"
            else:
                return "the Room in Progress until {}".format(book.date_to)
        else:
            return "available"
            
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
    
rate_values = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]
class PropertyRate(models.Model):
    rate = models.IntegerField(choices=rate_values, default=0)
    owner = models.ForeignKey(User, related_name="rate_owner", on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name="property_rates", on_delete=models.CASCADE)
    feedback = models.TextField(max_length=200, default="")
    def __str__(self):
        return self.property.title
    
    
class PropertyReservation(models.Model):
    owner = models.ForeignKey(User, related_name="reservation_owner", on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name="property_reservation", on_delete=models.CASCADE)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    guest = models.IntegerField(choices=rate_values, default=1)
    children = models.IntegerField(choices=rate_values, default=1)
    
    def in_progress(self):
        now = timezone.now().date()
        return now > self.date_to and now < self.date_from
    
    in_progress.boolean = True

class Category(models.Model):
    icon = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name
    

