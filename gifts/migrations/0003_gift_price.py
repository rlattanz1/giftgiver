# Generated by Django 4.2.8 on 2023-12-22 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0002_gift_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
