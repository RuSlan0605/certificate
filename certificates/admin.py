from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'full_name', 'date', ]
    list_display_links = ['id', 'full_name']
    prepopulated_fields = {'slug':('full_name', )}
