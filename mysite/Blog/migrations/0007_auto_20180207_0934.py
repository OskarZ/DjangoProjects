# Generated by Django 2.0.1 on 2018-02-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20180207_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='mail',
            field=models.CharField(max_length=40),
        ),
    ]