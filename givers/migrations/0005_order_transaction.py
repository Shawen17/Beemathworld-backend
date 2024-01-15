# Generated by Django 4.1.1 on 2022-10-02 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('givers', '0004_charge_destinationcharge_alter_give_gift_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(blank=True, max_length=50, null=True)),
                ('item', models.JSONField(default=list, null=True)),
                ('ordered_by', models.CharField(max_length=130, null=True)),
                ('ordered_on', models.DateTimeField(auto_now_add=True)),
                ('delivery_address', models.TextField()),
                ('contact_number', models.BigIntegerField()),
                ('amount', models.IntegerField(null=True)),
                ('paid', models.BooleanField(default=False)),
                ('packed', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
                ('dispatch_partner', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(default='', max_length=254)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('items', models.JSONField(default=list, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]