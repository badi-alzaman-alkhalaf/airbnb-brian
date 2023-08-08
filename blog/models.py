from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, related_name="post_author", verbose_name=_("author"),on_delete=models.CASCADE)
    title = models.TextField(max_length=255, verbose_name=_("title"))
    description = models.TextField(max_length=1000, verbose_name=_("description"))
    image = models.ImageField(upload_to='post_images', verbose_name=_("image"))
    date = models.DateField(default=timezone.now, verbose_name=_("date"))
    tags = TaggableManager()
    categories = models.ManyToManyField("Category",related_name="post_category", blank=True, verbose_name=_("categories"))
    slug = models.SlugField(verbose_name='slug' ,blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)    
        super(Post, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
    
class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(('slug') ,blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)    
        super(Category, self).save(*args, **kwargs) # Call the real save() method
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")

    def __str__(self):
        return self.name





# class Comments(models.Model):
#     author = models.ForeignKey(User, related_name='comment_author', on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE)
#     text = models.TextField(_(""), max_length="255", default='')
#     class Meta:
#         verbose_name = _("Comments")
#         verbose_name_plural = _("Commentss")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("comments_detail", kwargs={"pk": self.pk})
