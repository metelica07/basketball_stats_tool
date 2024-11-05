"""
Clean Data Function
Create a clean_data function. This function should perform the following actions:

Read the existing player data from the PLAYERS constants provided in constants.py
Clean the player data using copy.deepcopy().
Save the cleaned data to a new collection.
Data to be cleaned:

Height: This should be saved as an integer
Experience: This should be saved as a boolean value (True or False)
HINT: Think Lists with nested Dictionaries might be one way.

NOTE
Ensure you do not directly modify the data in PLAYERS or TEAMS constants. 
This data you should iterate and read from to build your own collection and would be 
ideal to clean the data as you loop over it building your new collection.
"""

#rom practice_data_cleaning_data import data #data is the list name here
#https://teamtreehouse.com/library/overwriting-data-in-python  read this for copy.deepcopy()
import copy
from constants import TEAMS
from constants import PLAYERS

all_players = copy.deepcopy(PLAYERS)
all_teams = copy.deepcopy(TEAMS)
total_team_number = int(len(TEAMS))


def clean_data():
    set_clean_player = []
    for cleandata in all_players:
        dic_clean_player = {}    
        dic_clean_player['name'] = cleandata['name']
        dic_clean_player['guardians'] = cleandata['guardians'].split(" and ")
        if cleandata['experience'] == 'YES':
            dic_clean_player['experience'] = 'TRUE'
        else:
            dic_clean_player['experience'] = 'FALSE'
        dic_clean_player['height'] = int(cleandata['height'].split()[0])
        set_clean_player.append(dic_clean_player)
    
    return set_clean_player

all_players_clean = copy.deepcopy(clean_data())

total_players_eachteam = int(len(PLAYERS) / len(TEAMS)) 
total_team_number = int(len(TEAMS))


def split_experience(all_players):
    exp_players_name = []
    nonexp_players_name = []
    for exp_players in all_players:
        if exp_players["experience"] == 'TRUE':
            exp_players_name.append(exp_players)
                
        else:
            nonexp_players_name.append(exp_players) 
    return (exp_players_name, nonexp_players_name)


def team_names():
    team_name_index = 1
    for each_team in all_teams:
        print(f"{team_name_index}) {each_team}")
        team_name_index += 1


def average_height(selected_team):
    total_height = 0
    for players in selected_team:
        total_height += players['height']

    team_ave_height = total_height / len(selected_team)

    return round(team_ave_height, 2)


def name_guardians(selected_team):
    players_name = [players['name'] for players in selected_team]
    players_string = ", ".join(players_name)

    guardians_name = []
    for guardians in selected_team:
        guardians_name += guardians['guardians']
    guardians_string = ", ".join(guardians_name)

    print(f"\nPlayers on Team: \n{players_string}")
    print(f"\nGuardians: \n{guardians_string}")


def balance_teams():
    exp_players_name, nonexp_players_name = split_experience(all_players_clean)
    teams_dic = {team: [] for team in all_teams}

    team_index = 0
    for player in exp_players_name:
        team_name = all_teams[team_index]
        teams_dic[team_name].append(player)
        team_index += 1

        if team_index == total_team_number:
            team_index = 0

    for player in nonexp_players_name:
        team_name = all_teams[team_index]
        teams_dic[team_name].append(player)
        team_index += 1

        if team_index == total_team_number:
            team_index = 0
    return teams_dic


def team_stat_output(selection):
    selected_team_name = all_teams[selection]
    balanced_team = balance_teams()
    selected_team = balanced_team[selected_team_name] 
    print(f"\nTeam: {selected_team_name} Stats")
    print("---------------------")
    print(f"Total Player: {len(selected_team)}")
    selected_team_exp_player, selected_team_noexp_player = split_experience(selected_team)
    print(f"Total experienced: {len(selected_team_exp_player)}")
    print(f"Total experienced: {len(selected_team_noexp_player)}")
    print(f"Average Height: {average_height(selected_team)}")
    name_guardians(selected_team)

if __name__ == "__main__":
    print("\nWELCOME TO BASKETBALL TEAM STATS TOOL")
    print("\n\n      --------MENU--------\n")
    while True:
        try:
            print("\nHere is your choises\n 1) Display Team Stats \n 2) Quit")
            first_select = int(input("\nPlease enter your option >  "))
            if first_select == 1:
                team_names()
                option = int(input("\nPlease select the team >  "))
                team_stat_output((option - 1))
                input("\nPlease press ENTER to continue...")
            elif first_select == 2:
                exit()
            else:
                print("\n***Please select valid options***")
        except ValueError:
            print("\n***Please select valid options***")











    


