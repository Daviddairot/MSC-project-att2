# Generated by Django 5.1.3 on 2024-11-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temperatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('temperature1', models.IntegerField(blank=True, default=0, null=True)),
                ('humidity1', models.IntegerField(blank=True, default=0, null=True)),
                ('temperature2', models.IntegerField(blank=True, default=0, null=True)),
                ('humidity2', models.IntegerField(blank=True, default=0, null=True)),
                ('temperature3', models.IntegerField(blank=True, default=0, null=True)),
                ('humidity3', models.IntegerField(blank=True, default=0, null=True)),
                ('temperature4', models.IntegerField(blank=True, default=0, null=True)),
                ('humidity4', models.IntegerField(blank=True, default=0, null=True)),
                ('temperature5', models.IntegerField(blank=True, default=0, null=True)),
                ('humidity5', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
