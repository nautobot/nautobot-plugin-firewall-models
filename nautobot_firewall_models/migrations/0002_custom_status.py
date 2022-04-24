# Generated by Django 3.2.13 on 2022-04-23 23:14

from django.db import migrations
import django.db.models.deletion
import nautobot.extras.models.statuses
import nautobot_firewall_models.models
from django.contrib.contenttypes.models import ContentType


def create_status(apps, schedma_editor):
    """Initial subset of statuses."""

    statuses = ["active", "staged", "decommissioned"]
    for i in statuses:
        status = nautobot.extras.models.statuses.Status.objects.get(slug=i)
        for model in apps.app_configs["nautobot_firewall_models"].get_models():
            ct = ContentType.objects.get_for_model(model)
            status.content_types.add(ct)


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0033_add__optimized_indexing"),
        ("nautobot_firewall_models", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(code=create_status),
        migrations.AlterField(
            model_name="addressobject",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_addressobject_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="addressobjectgroup",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_addressobjectgroup_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="addresspolicyobject",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_addresspolicyobject_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="destination",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_destination_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="fqdn",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_fqdn_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="iprange",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_iprange_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="policy",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_policy_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_policyrule_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="serviceobject",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_serviceobject_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="serviceobjectgroup",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_serviceobjectgroup_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="servicepolicyobject",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_servicepolicyobject_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="source",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_source_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="userobject",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_userobject_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="userobjectgroup",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_userobjectgroup_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="userpolicyobject",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_userpolicyobject_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="zone",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.models.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_zone_related",
                to="extras.status",
            ),
        ),
    ]
