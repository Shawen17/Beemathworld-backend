# Generated by Django 4.1.1 on 2022-10-07 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('givers', '0007_alter_user_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='items',
        ),
    ]
