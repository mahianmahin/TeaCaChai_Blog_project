# Generated by Django 3.2 on 2021-07-26 10:49

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tea_App', '0024_auto_20210726_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypesOfTea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tea_picture', models.ImageField(upload_to='tea_types')),
                ('type_name', models.CharField(max_length=100, null=True)),
                ('tea_description', ckeditor.fields.RichTextField()),
                ('first_section', models.BooleanField(default=False)),
                ('second_section', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 26, 16, 49, 40, 577483)),
        ),
    ]
