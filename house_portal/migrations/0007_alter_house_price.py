# Generated by Django 4.2.15 on 2024-08-24 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_portal', '0006_alter_house_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
