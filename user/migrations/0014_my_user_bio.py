# Generated by Django 3.1.1 on 2020-10-14 16:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_remove_my_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_user',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
