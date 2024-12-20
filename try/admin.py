from django.contrib import admin
from .models import User, Question

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'role', 'is_staff')
    search_fields = ('first_name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'correct_answer')
    search_fields = ('question',)
