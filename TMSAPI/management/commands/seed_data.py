from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from TMSAPI.models import Task
from datetime import date
import random

User = get_user_model()

class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **kwargs):
        # Create Superuser
        superuser, created = User.objects.get_or_create(username="admin", defaults={
            "email": "admin@example.com",
            "is_superuser": True,
            "is_staff": True
        })
        superuser.set_password("abc@2025")
        superuser.save()

        # Create Manager User
        manager, created = User.objects.get_or_create(username="manager1", defaults={
            "email": "manager@example.com",
            "is_staff": True
        })
        manager.set_password("abc@2025")
        manager.save()

        # Create Regular Users
        for i in range(3):
            user, created = User.objects.get_or_create(username=f"user{i+1}", defaults={
                "email": f"user{i+1}@example.com",
            })
            user.set_password("abc@2025")
            user.save()

        users = User.objects.filter(is_staff=False)

        # Create Tasks
        for i in range(5):
            task = Task.objects.create(
                title=f"Task {i+1}",
                description=f"This is task {i+1}",
                assignee=random.choice(users),
                due_date=date(2025, 3, random.randint(1, 30)),
                status="pending"
            )
            task.save()

        self.stdout.write(self.style.SUCCESS("Database successfully seeded!"))
