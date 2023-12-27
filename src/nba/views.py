from django_filters import rest_framework as filters
from rest_framework import status, viewsets
from rest_framework.response import Response

from .filters import TeamFilter
from .models import Team
from .serializers import TeamSerializer


class TeamsAPIView(viewsets.GenericViewSet):
    """
    A viewset for handling operations related to teams.

    list:
    Retrieve a list of all teams.

    """

    queryset = Team.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TeamFilter

    def list(self, request):
        """
        Get a list of all teams and return the serialized data.

        Returns:
            Response: A JSON response with the serialized data of all teams.
        """
        serializer = TeamSerializer(Team.objects(), many=True).data
        return Response(data=serializer, status=status.HTTP_200_OK)
