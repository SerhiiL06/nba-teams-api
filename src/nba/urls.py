from django.urls import path

from . import views

app_name = "nba"

urlpatterns = [
    path("teams/", views.TeamsAPIView.as_view({"get": "list"}), name="team-list")
]
