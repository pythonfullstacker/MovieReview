# Generated by Django 4.2.11 on 2024-05-06 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='m',
            old_name='year',
            new_name='date',
        ),
        migrations.AddField(
            model_name='m',
            name='actor',
            field=models.CharField(default='Unknown Actor', max_length=100),
        ),
        migrations.AddField(
            model_name='m',
            name='category',
            field=models.CharField(default='Unknown category', max_length=100),
        ),
    ]