# Generated by Django 3.2.20 on 2023-07-24 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20230722_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/images/default.jpg', upload_to='blog/'),
        ),
    ]