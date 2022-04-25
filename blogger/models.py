from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogger:getCategory', args=[self.slug])

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()
    slug = models.SlugField(max_length=40, unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True, through='CategoryToPost')
    post_picture = models.URLField(blank=True, null=True) #image

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogger:getPost',args=[self.slug])

class CategoryToPost(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)