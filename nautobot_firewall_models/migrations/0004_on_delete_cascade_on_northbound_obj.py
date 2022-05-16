# Generated by Django 3.2.13 on 2022-05-13 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("nautobot_firewall_models", "0003_default_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="addressobjectgroupm2m",
            name="address_group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.addressobjectgroup"
            ),
        ),
        migrations.AlterField(
            model_name="destaddrgroupm2m",
            name="pol_rule",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.policyrule"
            ),
        ),
        migrations.AlterField(
            model_name="destaddrm2m",
            name="pol_rule",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.policyrule"
            ),
        ),
        migrations.AlterField(
            model_name="fqdnipaddressm2m",
            name="fqdn",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.fqdn"),
        ),
        migrations.AlterField(
            model_name="policydevicem2m",
            name="policy",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.policy"),
        ),
        migrations.AlterField(
            model_name="policydynamicgroupm2m",
            name="policy",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.policy"),
        ),
        migrations.AlterField(
            model_name="policyrulem2m",
            name="policy",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.policy"),
        ),
        migrations.AlterField(
            model_name="serviceobjectgroupm2m",
            name="service_group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.serviceobjectgroup"
            ),
        ),
        migrations.AlterField(
            model_name="srcaddrgroupm2m",
            name="pol_rule",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.policyrule"
            ),
        ),
        migrations.AlterField(
            model_name="srcaddrm2m",
            name="pol_rule",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.policyrule"
            ),
        ),
        migrations.AlterField(
            model_name="srcusergroupm2m",
            name="pol_rule",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.policyrule"
            ),
        ),
        migrations.AlterField(
            model_name="srcuserm2m",
            name="pol_rule",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.policyrule"
            ),
        ),
        migrations.AlterField(
            model_name="svcgroupm2m",
            name="pol_rule",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.policyrule"
            ),
        ),
        migrations.AlterField(
            model_name="svcm2m",
            name="pol_rule",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.policyrule"
            ),
        ),
        migrations.AlterField(
            model_name="userobjectgroupm2m",
            name="user_group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.userobjectgroup"
            ),
        ),
        migrations.AlterField(
            model_name="zoneinterfacem2m",
            name="zone",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.zone"),
        ),
        migrations.AlterField(
            model_name="zonevrfm2m",
            name="zone",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.zone"),
        ),
    ]