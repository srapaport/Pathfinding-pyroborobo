# Projet "robotique" IA&Jeux 2021
#
import math
# Binome:
#  Prénom Nom: Léonard Moreau
#  Prénom Nom: Solal Rapaport

def get_team_name():
    return "[ team Genetique ]" # à compléter (comme vous voulez)

param = [0, 0, 1, 0, -1, 0, 0, 1, 1, 1, 1, -1, 0, 1]

def step(robotId, sensors):

    global param

    translation = math.tanh ( param[0] + param[1] * sensors["sensor_front_left"]["distance"] + param[2] * sensors["sensor_front"]["distance"] + param[3] * sensors["sensor_front_right"]["distance"] + (param[8] * sensors["sensor_front_left"]["distance"])/2 + (param[9] * sensors["sensor_front"]["distance"])/2 + (param[10] * sensors["sensor_front_right"]["distance"])/2)
    rotation = math.tanh ( param[4] + param[5] * sensors["sensor_front_left"]["distance"] + param[6] * sensors["sensor_front"]["distance"] + param[7] * sensors["sensor_front_right"]["distance"] + (param[11] * sensors["sensor_front_left"]["distance"])/2 + (param[12] * sensors["sensor_front"]["distance"])/2 + (param[13] * sensors["sensor_front_right"]["distance"])/2 )

    return translation, rotation
