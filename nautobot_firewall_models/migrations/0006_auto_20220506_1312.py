# Generated by Django 3.2.13 on 2022-05-06 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nautobot_firewall_models", "0005_auto_20220506_1312"),
    ]

    operations = [
        migrations.AlterField(
            model_name="policyrule",
            name="destination_address",
            field=models.ManyToManyField(
                related_name="destination_policy_rules", to="nautobot_firewall_models.AddressObject"
            ),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="destination_address_group",
            field=models.ManyToManyField(
                related_name="destination_policy_rules", to="nautobot_firewall_models.AddressObjectGroup"
            ),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="service",
            field=models.ManyToManyField(related_name="policy_rules", to="nautobot_firewall_models.ServiceObject"),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="service_group",
            field=models.ManyToManyField(related_name="policy_rules", to="nautobot_firewall_models.ServiceObjectGroup"),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="source_address",
            field=models.ManyToManyField(
                related_name="source_policy_rules", to="nautobot_firewall_models.AddressObject"
            ),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="source_address_group",
            field=models.ManyToManyField(
                related_name="source_policy_rules", to="nautobot_firewall_models.AddressObjectGroup"
            ),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="source_user",
            field=models.ManyToManyField(related_name="policy_rules", to="nautobot_firewall_models.UserObject"),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="source_user_group",
            field=models.ManyToManyField(related_name="policy_rules", to="nautobot_firewall_models.UserObjectGroup"),
        ),
    ]