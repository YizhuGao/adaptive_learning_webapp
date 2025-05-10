from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'can_take_experimental_test')
    list_filter = ('can_take_experimental_test',)
    search_fields = ('user__username', 'user__email')
