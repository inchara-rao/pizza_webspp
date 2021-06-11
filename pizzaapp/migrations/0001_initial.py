# Generated by Django 3.2.3 on 2021-06-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=10)),
                ('phoneno', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('phoneno', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('ordereditems', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
