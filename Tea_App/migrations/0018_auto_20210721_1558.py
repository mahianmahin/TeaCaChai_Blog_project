# Generated by Django 3.2 on 2021-07-21 09:58

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tea_App', '0017_alter_blog_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteutilities',
            name='description',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siteutilities',
            name='footer_text',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 21, 15, 58, 9, 31731)),
        ),
    ]
