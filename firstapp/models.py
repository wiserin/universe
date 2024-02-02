from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
    
class Articles(models.Model):
    autor = models.CharField(max_length=30)
    data = models.CharField(max_length=20)
    time = models.CharField(max_length=10)
    topic = models.CharField(max_length=20)
    heading = models.CharField(max_length=50)
    content = HTMLField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

