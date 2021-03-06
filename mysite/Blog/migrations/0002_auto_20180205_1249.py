# Generated by Django 2.0.1 on 2018-02-05 11:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Reisen', 'Reisen'), ('Arbeit', 'Arbeit'), ('Freizeit', 'Freizeit'), ('Andere', 'Andere')], default='Andere', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
