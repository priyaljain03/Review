# Generated by Django 3.2.8 on 2021-11-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='D:\\Vini Projects\\projects\\Review\\static\\images'),
        ),
    ]