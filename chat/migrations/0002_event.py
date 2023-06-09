# Generated by Django 4.2.1 on 2023-05-12 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='event_images/')),
                ('ticket_fee', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('place', models.CharField(max_length=255)),
                ('seat', models.CharField(max_length=255)),
            ],
        ),
    ]
