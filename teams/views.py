from django.shortcuts import render
from .models import Team, Player
from .forms import TeamForm, PlayerForm
from django.shortcuts import render, redirect


def all_teams(request):
    teams = Team.objects.all()
    players = Player.objects.all()

    context = {'teams': teams, "players": players}
    return render(request, "../Templates/teams/all_teams.html", context)


def all_players(request):
    players = Player.objects.order_by('name')

    context = {'players': players}
    return render(request, "../Templates/teams/all_players.html", context)


def create_team(request):
    if request.method == 'POST':
        team_form = TeamForm(request.POST)
        player_form1 = PlayerForm(request.POST, prefix='player1')
        player_form2 = PlayerForm(request.POST, prefix='player2')
        if team_form.is_valid() and player_form1.is_valid() and player_form2.is_valid():
            team = team_form.save()
            player1 = player_form1.save(commit=False)
            player1.team = team
            player1.save()
            player2 = player_form2.save(commit=False)
            player2.team = team
            player2.save()
            return redirect('all_teams')  # Replace 'team_list' with the appropriate URL name
    else:
        team_form = TeamForm()
        player_form1 = PlayerForm(prefix='player1')
        player_form2 = PlayerForm(prefix='player2')
    return render(request, '../Templates/teams/create_team.html',
                  {'team_form': team_form, 'player_form1': player_form1, 'player_form2': player_form2})
