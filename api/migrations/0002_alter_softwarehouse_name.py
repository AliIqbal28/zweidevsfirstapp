# Generated by Django 4.1 on 2022-08-15 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softwarehouse',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
