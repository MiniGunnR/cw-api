# Generated by Django 2.0.6 on 2018-06-30 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20180630_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='image',
        ),
    ]
