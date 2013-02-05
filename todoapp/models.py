from django.db import models

# Create your models here.
class ToDoList(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    dt = models.DateTimeField(auto_now_add=True)
