# Generated by Django 3.1.1 on 2020-10-14 16:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20201012_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_user',
            name='bio',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
