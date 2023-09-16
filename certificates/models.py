from django.db import models

    
class Student(models.Model):
    full_name = models.CharField(
        max_length=200,
        help_text='Enter a full name'
    )
    slug = models.SlugField()
    mentor = models.CharField(max_length=100, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(
        help_text='Enter a date'
    )
    certificate = models.ImageField(
        upload_to='student/%Y/%m/%d',
        blank=True,
        null=True)

    def __str__(self) -> str:
        return self.full_name