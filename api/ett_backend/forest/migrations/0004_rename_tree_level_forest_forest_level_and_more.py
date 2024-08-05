# Generated by Django 5.0.7 on 2024-07-19 07:30

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forest", "0003_alter_forest_table"),
    ]

    operations = [
        migrations.RenameField(
            model_name="forest",
            old_name="tree_level",
            new_name="forest_level",
        ),
        migrations.AlterField(
            model_name="forest",
            name="forest_uuid",
            field=models.UUIDField(db_index=True, default=uuid.uuid4, unique=True),
        ),
    ]
