# Generated by Django 4.1.5 on 2023-03-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0002_proj_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='proj',
            name='code',
            field=models.CharField(default='default_value', max_length=255),
        ),
    ]
