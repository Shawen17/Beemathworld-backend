# Generated by Django 4.1.1 on 2022-10-20 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('givers', '0020_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopper', models.CharField(max_length=100)),
                ('quantity_in_cart', models.IntegerField()),
                ('status', models.BooleanField(choices=[('in-cart', 'in-cart'), ('ordered', 'ordered')], default='in-cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='givers.product')),
            ],
        ),
    ]