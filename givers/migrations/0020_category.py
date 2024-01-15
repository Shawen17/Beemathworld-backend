# Generated by Django 4.1.1 on 2022-10-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('givers', '0019_rename_date_posted_product_uploaded_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
    ]
