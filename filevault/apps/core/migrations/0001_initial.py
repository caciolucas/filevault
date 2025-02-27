# Generated by Django 5.1.4 on 2024-12-17 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('client_id', models.CharField(max_length=50, unique=True)),
                ('client_secret', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('mime_type', models.CharField(max_length=255, null=True, verbose_name='Mime_type')),
                ('size', models.FloatField(null=True, verbose_name='Size')),
                ('path', models.FileField(upload_to='')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.client')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
