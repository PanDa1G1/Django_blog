from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from mdeditor.fields import MDTextField
# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='parent_category')

    def get_absolute_url(self):
        return reverse("blog:{}".format(self.slug))

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Articles(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = MDTextField(verbose_name="body")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = TaggableManager()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='blog_category')

    def get_absolute_url(self):
        return reverse("blog:article_details", args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    objects = models.Manager()  # 默认的管理器

    class Meta:
        ordering = ('-publish',)


    def __str__(self):
        return self.title