# Generated by Django 3.2.8 on 2021-11-07 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_avgrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='avgRating',
            field=models.IntegerField(default=0),
        ),
    ]