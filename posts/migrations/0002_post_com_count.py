# Generated by Django 4.2.8 on 2024-01-04 09:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="com_count",
            field=models.IntegerField(default=0),
        ),
    ]
