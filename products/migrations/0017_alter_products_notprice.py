# Generated by Django 4.1.7 on 2023-03-16 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_products_notprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='notprice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
