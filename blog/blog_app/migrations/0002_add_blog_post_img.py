# Generated by Django 3.0.8 on 2020-07-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_blog',
            name='post_img',
            field=models.ImageField(default=0, upload_to='images'),
            preserve_default=False,
        ),
    ]
