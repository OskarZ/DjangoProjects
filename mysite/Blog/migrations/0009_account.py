# Generated by Django 2.0.1 on 2018-02-07 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_auto_20180207_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=40)),
                ('passwort', models.CharField(max_length=20)),
            ],
        ),
    ]
