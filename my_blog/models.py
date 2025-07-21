from django.db import models
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    about=models.CharField(max_length=500)
    image=models.ImageField(upload_to='image/', blank=True,null=True)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
# class Students(models.Model):
#     name=models.CharField(max_length=20)
#     age=models.PositiveIntegerField()
#     marks=models.PositiveBigIntegerField()

