# Generated by Django 4.1.4 on 2023-01-14 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NonVegInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Burger', models.CharField(max_length=40)),
                ('prize', models.IntegerField()),
            ],
        ),
    ]
