# Generated by Django 4.1.7 on 2023-03-12 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_customer_info_myid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_info',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer_info',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
