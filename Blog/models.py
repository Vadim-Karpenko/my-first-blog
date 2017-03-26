from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    short_text = models.CharField(max_length=600)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.safe()
        
    def __str__(self):
        return self.title