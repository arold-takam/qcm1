from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]

    phone = models.CharField(max_length=50, unique=True, null=False, blank=False)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.username} : ({self.role})"


class Question(models.Model):
    question = models.CharField(max_length=255, null=False, blank=False)
    correct_answer = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"Question : {self.question}"

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, blank=False)
    answer = models.CharField(max_length=255, null=False, blank=False)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.question}: {self.answer} ({'Correct' if self.is_correct else 'Wrong'})"