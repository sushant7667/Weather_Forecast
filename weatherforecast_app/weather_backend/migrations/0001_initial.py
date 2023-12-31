# Generated by Django 4.2.3 on 2023-07-12 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather_Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('detailing_type', models.CharField(choices=[('Hourly', 'Hourly'), ('Daily', 'Daily')], max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('isactive', models.BooleanField(default=True)),
            ],
        ),
    ]
