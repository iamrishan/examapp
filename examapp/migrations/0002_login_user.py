# Generated by Django 3.0 on 2020-01-31 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='user',
            field=models.CharField(default='student', max_length=15),
        ),
    ]
