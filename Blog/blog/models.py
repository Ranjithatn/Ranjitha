from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class CustomerManager(models.Manager):
       def get_queryset(self):
           return super().get_queryset().filter(status='published')

class Post(models.Model):
    #status=models.CharField(max_length=10,choices=status_choices,default='draft')
    status_choices=(('draft','Draft'),('published','published'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=254,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)#date of publish
    created=models.DateTimeField(auto_now_add=True)#time when this post is created
    updated=models.DateTimeField(auto_now=True)#at what time save method is called
    #above 2 are automatically considered
    status=models.CharField(max_length=10,choices=status_choices,default='draft')
    objects=CustomerManager()
    tags=TaggableManager()

    class Meta:
        ordering=('-publish',)#for descending order if we call post.objects.all()then it will come in ascending order for that we use - for descening order

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])



class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=32)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=('created',)
    def __str__(self):
        return 'Commented By {} on {}.format(self.name,self.post)'