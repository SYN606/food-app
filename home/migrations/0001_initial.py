# Generated by Django 4.1.7 on 2023-03-19 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Create_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField(default=0)),
            ],
        ),
    ]