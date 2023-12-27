from django.test import TestCase
from django.urls import reverse


class TeamTestCase(TestCase):
    def test_team_list(self):
        path = reverse("nba:team-list")
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 90)
