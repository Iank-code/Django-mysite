from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=200)
    
    def _str_(self):
        return self.name
    
    
class Item(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    
    def _str_(self):
        return self.text