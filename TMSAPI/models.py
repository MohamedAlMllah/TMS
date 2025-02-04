from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=255, db_index=True)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='assigned_user', null=True)
    due_date = models.DateField(default=date.today)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', db_index=True)
    dependencies = models.ManyToManyField('self', symmetrical=False, blank=True)
    
    def can_be_completed(self):
        """Check if all dependencies are completed before allowing this task to be completed."""
        return not self.dependencies.exclude(status='completed').exists()

    def __str__(self):
        return self.title
    