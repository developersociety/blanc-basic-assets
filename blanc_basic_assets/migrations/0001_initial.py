# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('file', models.FileField(upload_to='assets/file')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='FileCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'file categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('file', models.ImageField(height_field='image_height', verbose_name='Image', upload_to='assets/image', width_field='image_width')),
                ('image_height', models.PositiveIntegerField(editable=False)),
                ('image_width', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='ImageCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'image categories',
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(to='assets.ImageCategory', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='file',
            name='category',
            field=models.ForeignKey(to='assets.FileCategory', on_delete=models.CASCADE),
        ),
    ]
