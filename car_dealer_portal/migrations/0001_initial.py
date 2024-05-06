# Generated by Django 4.2.11 on 2024-05-01 18:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.CharField(max_length=6, unique=True, validators=[django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(6)])),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_name', models.CharField(max_length=50)),
                ('bedrooms', models.PositiveIntegerField()),
                ('bathrooms', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=300)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car_dealer_portal.area')),
            ],
        ),
        migrations.CreateModel(
            name='CarDealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(13)])),
                ('wallet', models.IntegerField(default=0)),
                ('area', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='car_dealer_portal.area')),
                ('car_dealer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]