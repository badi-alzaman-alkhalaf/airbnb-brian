from distutils.command.upload import upload
from numbers import Integral
from turtle import title
from django.db import models

# Create your models here.

class About(models.Model):
    image = models.ImageField(upload_to="about/")
    what_we_do = models.TextField(max_length=1000)
    our_mission = models.TextField(max_length=1000)
    our_goal = models.TextField(max_length=1000)
    why_you_choose_us = models.TextField(max_length=1000)
    

    class Meta:
        verbose_name = ("About")
        verbose_name_plural = ("Abouts")

    def __str__(self):
        return self.id
    
class Faq(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    class Meta:
        verbose_name = ("Faq")
        verbose_name_plural = ("Faqs")

    def __str__(self):
        return self.title
    
    
class Info(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='info/')
    descrpition = models.TextField(max_length=1000)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)
    fb_url = models.URLField(max_length=200)
    tw_url = models.URLField(max_length=200)
    in_url = models.URLField(max_length=200)
    email = models.EmailField(max_length=254)
    

    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")

    def __str__(self):
        return self.name
