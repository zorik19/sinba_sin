# Generated by Django 3.2.3 on 2021-06-01 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_post/'),
        ),
    ]
