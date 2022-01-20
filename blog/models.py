from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150)
    excerpt=models.CharField(max_length=150)
    image_name=models.CharField(max_length=150)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True,db_index=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    





