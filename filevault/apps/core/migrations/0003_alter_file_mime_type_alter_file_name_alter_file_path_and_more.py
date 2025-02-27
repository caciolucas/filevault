# Generated by Django 5.1.4 on 2024-12-17 20:03

import private_storage.fields
import private_storage.storage.files
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_client_id_alter_file_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='mime_type',
            field=models.CharField(default='', max_length=255, verbose_name='Mime_type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='path',
            field=private_storage.fields.PrivateFileField(storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='', verbose_name='Path'),
        ),
        migrations.AlterField(
            model_name='file',
            name='size',
            field=models.BigIntegerField(default=1, verbose_name='Size'),
            preserve_default=False,
        ),
    ]
