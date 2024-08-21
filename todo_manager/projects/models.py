from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    # list_of_todos = models.CharField(max_length=255) 
    # list_of_todos = models.TextField(default='{}')  # JSON string storing todos
    
    def completed_todos(self):
        return self.todos.filter(status = True)
    
    def pending_todos(self):
        return self.todos.filter (status = False)
    
    def __str__(self):
        return self.title

class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255, blank = True, null=True)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
