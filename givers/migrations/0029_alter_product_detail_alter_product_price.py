# Generated by Django 4.1.1 on 2022-11-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('givers', '0028_product_on_sales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
