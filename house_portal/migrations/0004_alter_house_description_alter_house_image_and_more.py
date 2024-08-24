# Generated by Django 4.2.15 on 2024-08-23 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house_portal', '0003_rename_house_name_house_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='house_images/'),
        ),
        migrations.AlterField(
            model_name='house',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_houses', to='house_portal.owner'),
        ),
        migrations.AlterField(
            model_name='house',
            name='type',
            field=models.CharField(choices=[('House', 'House'), ('Hotel', 'Hotel'), ('Restaurant', 'Restaurant')], default='House', max_length=20),
        ),
    ]