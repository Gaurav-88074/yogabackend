# Generated by Django 4.1 on 2022-12-10 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_person_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
