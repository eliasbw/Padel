from django.urls import path
from . import views


urlpatterns = [
    path('t', views.all_teams, name='all_teams'),
    path('p', views.all_players, name='all_players'),
    path('create', views.create_team, name='create_team'),

]
