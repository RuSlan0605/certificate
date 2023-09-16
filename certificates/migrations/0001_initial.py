# Generated by Django 4.2.4 on 2023-08-15 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(help_text='Enter a full name', max_length=200)),
                ('date', models.DateField(help_text='Enter a date')),
            ],
        ),
    ]
