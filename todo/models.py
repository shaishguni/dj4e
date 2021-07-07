from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField()
    # description = models.TextField()
    
    def __str__(self):
        return self.name