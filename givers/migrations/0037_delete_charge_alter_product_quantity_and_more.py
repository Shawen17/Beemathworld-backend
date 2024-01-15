# Generated by Django 4.1.1 on 2023-01-09 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('givers', '0036_alter_store_unit_sold'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Charge',
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='store',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='store', to='givers.product'),
        ),
        migrations.AlterField(
            model_name='store',
            name='unit_added',
            field=models.IntegerField(default=0),
        ),
    ]