# Generated by Django 4.2.1 on 2023-05-13 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_course_credits'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='Unknown'),
        ),
    ]
