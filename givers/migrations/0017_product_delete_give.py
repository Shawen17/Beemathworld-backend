# Generated by Django 4.1.1 on 2022-10-18 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('givers', '0016_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, choices=[('furniture', 'Furniture'), ('clothe', 'Clothes'), ('shoe', 'Shoes'), ('toy', 'toys'), ('electronics', 'Electronics'), ('bag', 'Bags'), ('mobile-phone', 'mobile-phones'), ('laptop', 'Laptops'), ('book', 'Books'), ('kitchen-utensil', 'Kitchen-utensils'), ('bicycle', 'Bicyle'), ('accessories', 'Accessories'), ('food-stuff', 'Food-stuffs'), ('grocery', 'Groceries'), ('generator', 'Generator'), ('beauty-product', 'Beauty-products'), ('native-wear', 'Natives')], default='', max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='givers/images/')),
                ('detail', models.CharField(blank=True, default='', max_length=200)),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField(default=0)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_requested', models.DateTimeField(blank=True, null=True)),
                ('date_received', models.DateTimeField(blank=True, null=True)),
                ('buyer', models.CharField(blank=True, default='', max_length=100)),
                ('state', models.CharField(choices=[('lagos', 'Lagos'), ('ogun', 'Ogun'), ('osun', 'Osun'), ('oyo', 'Oyo'), ('ondo', 'Ondo'), ('kwara', 'Kwara'), ('niger', 'Niger'), ('nassarawa', 'Nassarawa'), ('plateau', 'Plateau'), ('abuja', 'Abuja'), ('edo', 'Edo'), ('abia', 'Abia'), ('akwa-ibom', 'Akwa-Ibom'), ('adamawa', 'Adamawa'), ('anambra', 'Anambra'), ('cross-river', 'Cross-River'), ('delta', 'Delta'), ('ebonyi', 'Ebonyi'), ('benue', 'Benue'), ('bayelsa', 'Bayelsa'), ('ekiti', 'Ekiti'), ('enugu', 'Enugu'), ('jigawa', 'Jigawa'), ('kano', 'Kano'), ('katsina', 'Katsina'), ('kogi', 'Kogi'), ('kebbi', 'Kebbi'), ('kaduna', 'Kaduna'), ('imo', 'Imo'), ('borno', 'Borno'), ('gombe', 'Gombe'), ('rivers', 'Rivers'), ('zamfara', 'Zamfara'), ('yobe', 'Yobe'), ('sokoto', 'Sokoto')], max_length=40)),
                ('status', models.CharField(blank=True, choices=[('unpicked', 'unpicked'), ('delivered', 'delivered'), ('on-delivery', 'on-delivery'), ('picked', 'picked'), ('paid', 'paid')], default='unpicked', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Give',
        ),
    ]
