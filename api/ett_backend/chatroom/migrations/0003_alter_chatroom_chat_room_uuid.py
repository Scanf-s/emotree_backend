# Generated by Django 5.0.7 on 2024-07-19 07:30

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatroom", "0002_alter_chatroom_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatroom",
            name="chat_room_uuid",
            field=models.UUIDField(db_index=True, default=uuid.uuid4, unique=True),
        ),
    ]
