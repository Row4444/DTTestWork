# Generated by Django 3.1.1 on 2020-09-24 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="like",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
