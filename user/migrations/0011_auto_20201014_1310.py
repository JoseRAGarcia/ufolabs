# Generated by Django 3.1.1 on 2020-10-14 16:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_my_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_user',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
