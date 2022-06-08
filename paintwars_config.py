# Nicolas
# 2021-03-31

# Arena
import paintwars_arena
get_arena = paintwars_arena.get_arena
arenaIndexSelector = 0 # numéro de l'arène, entre 0 et 4

# Starting position
invertStartingPosition = False # True: red commence à gauche. Sinon, commence à droite.

# Red team
# import paintwars_team_champion
# get_name_red_team = paintwars_team_champion.get_team_name
# step_red_team = paintwars_team_champion.step
# import paintwars_team_braitenberg
# get_name_red_team = paintwars_team_braitenberg.get_team_name
# step_red_team = paintwars_team_braitenberg.step
#import paintwars_team_genetique
#get_name_red_team = paintwars_team_genetique.get_team_name
#step_red_team = paintwars_team_genetique.step
import paintwars_team_subsomption
get_name_red_team = paintwars_team_subsomption.get_team_name
step_red_team = paintwars_team_subsomption.step

# Blue team
# import paintwars_team_braitenberg
# get_name_blue_team = paintwars_team_braitenberg.get_team_name
# step_blue_team = paintwars_team_braitenberg.step
import paintwars_team_champion
get_name_blue_team = paintwars_team_champion.get_team_name
step_blue_team = paintwars_team_champion.step
# import paintwars_team_genetique
# get_name_blue_team = paintwars_team_genetique.get_team_name
# step_blue_team = paintwars_team_genetique.step

# Simulation mode: realtime=0, fast=1, super_fast_no_render=2
simulation_mode = 2
