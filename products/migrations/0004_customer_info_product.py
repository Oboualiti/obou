# Generated by Django 4.1.7 on 2023-03-12 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_info',
            name='product',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
    ]
