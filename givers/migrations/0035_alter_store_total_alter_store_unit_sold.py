# Generated by Django 4.1.1 on 2023-01-08 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('givers', '0034_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='store',
            name='unit_sold',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]