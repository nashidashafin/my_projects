# Generated by Django 4.1.3 on 2023-01-16 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-02-12'),
            preserve_default=False,
        ),
    ]
