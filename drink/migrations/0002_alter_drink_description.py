# Generated by Django 5.0 on 2023-12-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='description',
            field=models.TextField(),
        ),
    ]
