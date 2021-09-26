# Generated by Django 3.0.6 on 2021-09-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZoneDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pinCode', models.IntegerField()),
                ('zoneType', models.CharField(max_length=50)),
                ('numCases', models.IntegerField()),
            ],
        ),
    ]