# Generated by Django 5.0 on 2024-08-23 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_guest_date_of_arrival_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='category',
        ),
    ]