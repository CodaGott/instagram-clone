# Generated by Django 3.2 on 2021-05-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='text',
            field=models.CharField(default=False, max_length=500),
        ),
    ]
