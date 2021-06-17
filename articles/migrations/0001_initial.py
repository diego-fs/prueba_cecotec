# Generated by Django 3.2.4 on 2021-06-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(editable=False, max_length=255, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('size', models.FloatField()),
                ('colour', models.CharField(max_length=25)),
            ],
        ),
    ]
