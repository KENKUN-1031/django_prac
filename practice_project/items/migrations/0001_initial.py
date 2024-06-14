# Generated by Django 4.2.2 on 2024-06-14 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=100)),
                ('itemPrice', models.IntegerField(default=0)),
                ('itemStocks', models.IntegerField(default=0)),
                ('itemCategory', models.CharField(max_length=100)),
            ],
        ),
    ]
