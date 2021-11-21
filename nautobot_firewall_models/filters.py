"""Filtering for VIP Tracker."""

from nautobot.extras.filters import CreatedUpdatedFilterSet
from nautobot.utilities.filters import BaseFilterSet, TagFilter

from nautobot_firewall_models import models


class IPRangeFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for IPRange."""

    class Meta:
        """Meta attributes for filter."""

        model = models.IPRange

        # fields = ["id", "start_address", "end_address", "vrf", "size", "description"]
        fields = ["id", "vrf", "size", "description"]


class FQDNFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for FQDN."""

    class Meta:
        """Meta attributes for filter."""

        model = models.FQDN

        fields = ["id", "name", "description"]


class AddressObjectFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for AddressObject."""

    class Meta:
        """Meta attributes for filter."""

        model = models.AddressObject

        fields = ["id", "name", "ip_address", "prefix", "ip_range", "fqdn", "description"]


class AddressObjectGroupFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for AddressObjectGroup."""

    class Meta:
        """Meta attributes for filter."""

        model = models.AddressObjectGroup

        fields = ["id", "name", "address_objects", "description"]


class AddressPolicyObjectFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for AddressPolicyObject."""

    class Meta:
        """Meta attributes for filter."""

        model = models.AddressPolicyObject

        fields = ["id", "name", "address_objects", "address_object_groups", "description"]


class ServiceObjectFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for ServiceObject."""

    class Meta:
        """Meta attributes for filter."""

        model = models.ServiceObject

        fields = ["id", "name", "slug", "ip_protocol", "port", "description"]


class ServiceObjectGroupFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for ServiceObjectGroup."""

    class Meta:
        """Meta attributes for filter."""

        model = models.ServiceObjectGroup

        fields = ["id", "name", "service_objects", "description"]


class ServicePolicyObjectFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for ServicePolicyObject."""

    class Meta:
        """Meta attributes for filter."""

        model = models.ServicePolicyObject

        fields = ["id", "name", "service_objects", "service_object_groups", "description"]


class UserObjectFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for UserObject."""

    class Meta:
        """Meta attributes for filter."""

        model = models.UserObject
        fields = ["id", "name", "username"]


class UserObjectGroupFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for UserObjectGroup."""

    class Meta:
        """Meta attributes for filter."""

        model = models.UserObjectGroup
        fields = ["id", "name", "user_objects", "description"]


class UserPolicyObjectFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for UserPolicyObject."""

    class Meta:
        """Meta attributes for filter."""

        model = models.UserPolicyObject

        fields = ["id", "name", "user_objects", "user_object_groups", "description"]


class ZoneFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for Zone."""

    class Meta:
        """Meta attributes for filter."""

        model = models.Zone

        fields = ["id", "name", "vrfs", "interfaces", "description"]


class SourceFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for Source."""

    class Meta:
        """Meta attributes for filter."""

        model = models.Source
        fields = [
            "id",
            "address",
            "user",
            "service",
            "zone",
            "description",
        ]


class DestinationFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for Destination."""

    class Meta:
        """Meta attributes for filter."""

        model = models.Destination
        fields = [
            "id",
            "address",
            "service",
            "zone",
            "description",
        ]


class PolicyRuleFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for PolicyRule."""

    tag = TagFilter()

    class Meta:
        """Meta attributes for filter."""

        model = models.PolicyRule
        fields = ["id", "index", "source", "destination", "action", "log"]


class PolicyFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    """Filter for Policy."""

    class Meta:
        """Meta attributes for filter."""

        model = models.Policy
        fields = ["id", "name", "description", "policy_rules"]