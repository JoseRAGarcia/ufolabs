# Generated by Django 3.1.1 on 2020-11-10 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_remove_post_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
