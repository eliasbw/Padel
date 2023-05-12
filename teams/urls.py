from django.urls import path
from . import views


urlpatterns = [
    path('all_teams', views.all_teams, name='all_teams'),
    path('all_players', views.all_players, name='all_players'),
    path('create', views.create_team, name='create_team'),
    path('delete/<int:team_id>', views.delete_team, name='delete_team'),
]
