# Generated by Django 4.2.7 on 2023-11-26 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
