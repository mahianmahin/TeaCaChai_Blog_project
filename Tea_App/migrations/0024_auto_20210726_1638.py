# Generated by Django 3.2 on 2021-07-26 10:38

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tea_App', '0023_auto_20210726_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteutilities',
            name='types_heading',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 26, 16, 38, 48, 293501)),
        ),
    ]