# Generated by Django 4.1.4 on 2022-12-18 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file',
            new_name='my_file',
        ),
    ]