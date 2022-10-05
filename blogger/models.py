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
    STATUS = (
        (0,"Draft"),
        (1,"Published")
        )
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    slug = models.SlugField(max_length=40, unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True, through='CategoryToPost')
    post_picture = models.URLField(blank=True, null=True) #image
    status = models.IntegerField(choices=STATUS, default=0)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogger:getPost',args=[self.slug])

class CategoryToPost(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

class Solutions(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image_url = models.URLField()
    action_form = models.TextField(blank= True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blogger:getSolution',args=[self.slug])

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.name)