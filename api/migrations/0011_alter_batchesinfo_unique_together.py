# Generated by Django 4.1 on 2022-12-10 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_batchesinfo_month'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='batchesinfo',
            unique_together={('person', 'month')},
        ),
    ]
