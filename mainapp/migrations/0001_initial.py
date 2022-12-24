# Generated by Django 4.0.8 on 2022-12-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
                ('flag_link', models.CharField(max_length=100)),
                ('capital', models.CharField(max_length=100)),
                ('largest_city', models.CharField(max_length=100)),
                ('official_languages', models.CharField(max_length=100)),
                ('area_total', models.CharField(max_length=30)),
                ('population', models.CharField(max_length=30)),
                ('GDP_nominal', models.CharField(max_length=30)),
            ],
        ),
    ]