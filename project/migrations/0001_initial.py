# Generated by Django 2.2.6 on 2020-08-16 11:22

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
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=150, unique=True)),
                ('profile', models.TextField()),
            ],
        ),
    ]
