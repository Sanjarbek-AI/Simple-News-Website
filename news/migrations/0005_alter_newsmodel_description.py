# Generated by Django 3.2 on 2021-04-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_newsmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='description',
            field=models.TextField(),
        ),
    ]