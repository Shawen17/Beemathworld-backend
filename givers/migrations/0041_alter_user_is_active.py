# Generated by Django 4.1.1 on 2023-05-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("givers", "0040_alter_user_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
    ]
