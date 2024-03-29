# Generated by Django 4.1.1 on 2022-10-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('givers', '0018_rename_amount_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='date_posted',
            new_name='uploaded',
        ),
        migrations.RemoveField(
            model_name='product',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_received',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_requested',
        ),
        migrations.RemoveField(
            model_name='product',
            name='state',
        ),
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
