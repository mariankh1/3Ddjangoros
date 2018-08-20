# Generated by Django 2.1 on 2018-08-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drone_name', models.CharField(max_length=100)),
                ('drone_id', models.IntegerField()),
                ('added_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DroneMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_name', models.CharField(max_length=200)),
                ('added_date', models.DateTimeField()),
            ],
        ),
    ]
