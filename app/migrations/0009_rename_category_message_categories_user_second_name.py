# Generated by Django 5.0 on 2024-08-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_guest_date_of_arrival_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='second_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
