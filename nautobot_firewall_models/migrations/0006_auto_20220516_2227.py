# Generated by Django 3.2.13 on 2022-05-16 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nautobot_firewall_models", "0005_auto_20220516_2110"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="serviceobject",
            unique_together={("port", "ip_protocol")},
        ),
        migrations.RemoveField(
            model_name="serviceobject",
            name="slug",
        ),
    ]