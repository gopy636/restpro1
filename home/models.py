from django.db import models

# Create your models here.
class  Todo(models.Model):
    task_name=models.CharField(max_length=100)
    task_descriptions=models.CharField(max_length=100)
    task_status=models.CharField(max_length=20,default='Incomplete')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

