# Generated by Django 4.1.1 on 2022-10-10 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('givers', '0013_order_item_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item_ids',
        ),
    ]
