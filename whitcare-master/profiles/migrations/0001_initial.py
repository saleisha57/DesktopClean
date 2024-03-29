# Generated by Django 2.0.2 on 2018-04-08 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=17)),
                ('available_weeknights', models.BooleanField()),
                ('available_weekends', models.BooleanField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
