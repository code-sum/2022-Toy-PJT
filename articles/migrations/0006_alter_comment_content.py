# Generated by Django 3.2.13 on 2022-10-18 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=80),
        ),
    ]