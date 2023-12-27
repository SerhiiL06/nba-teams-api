import django_filters
import django_mongoengine_filter

from .models import Team


class TeamFilter(django_mongoengine_filter.FilterSet):
    class Meta:
        model = Team
        fields = ["simple_name"]
