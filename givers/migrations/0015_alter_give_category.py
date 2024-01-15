# Generated by Django 4.1.1 on 2022-10-10 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('givers', '0014_remove_order_item_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='give',
            name='category',
            field=models.CharField(blank=True, choices=[('furniture', 'Furniture'), ('clothe', 'Clothes'), ('shoe', 'Shoes'), ('toy', 'toys'), ('electronics', 'Electronics'), ('bag', 'Bags'), ('mobile-phone', 'mobile-phones'), ('laptop', 'Laptops'), ('book', 'Books'), ('kitchen-utensil', 'Kitchen-utensils'), ('bicycle', 'Bicyle'), ('accessories', 'Accessories'), ('food-stuff', 'Food-stuffs'), ('grocery', 'Groceries'), ('generator', 'Generator'), ('beauty-product', 'Beauty-products'), ('native-wear', 'Natives')], default='', max_length=50),
        ),
    ]