# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Solal Rapaport
#  Prénom Nom: Léonard Moreau

import math
param = [0, 0, 1, 0, -1, 0, 0, 1, 1, 1, 1, -1, 0, 1]

def get_team_name():
    return "[ RapMor ]" # à compléter (comme vous voulez)


def step_braitenberg(robotId, sensors):

    translation = 1 # vitesse de translation (entre -1 et +1)
    rotation = 0 # vitesse de rotation (entre -1 et +1)

    weight_left = 0
    weight_right = 0

    ###
    ##  On ne tourne le robot que s'il repère un ennemie
    ##  On veut que le robot suive son ennemie    
    ###

    ################ BRAITENBERG 1ER REPULSIF -> ALLIE
    ################ BRAITENBERG APPAT -> ENNEMIE

    if sensors["sensor_front"]["isRobot"] == True:                                                        #Le sensor detecte un robot
        if sensors["sensor_front"]["isSameTeam"] == True and sensors["sensor_front"]["distance"] < 1:    #Le robot est un robot allié que je suis (suivre) potentiellement
            weight_right += 1 + sensors["sensor_front_left"]["distance"]

    ################ LEFT SIDE

    if sensors["sensor_front_left"]["isRobot"] == True:                                                             #Le sensor detecte un robot
        if sensors["sensor_front_left"]["isSameTeam"] == False and sensors["sensor_front_left"]["distance"] < 1:    #Le robot est un robot ennemie
            weight_left += sensors["sensor_front_left"]["distance"]
        else:                                                                                                       #Le robot est un robot allie
            weight_left -= (1 +  sensors["sensor_front_left"]["distance"])

    if sensors["sensor_left"]["isRobot"] == True:                                                                   #Le sensor detecte un robot
        if sensors["sensor_left"]["isSameTeam"] == False and sensors["sensor_left"]["distance"] < 1:                #Le robot est un robot ennemie
            weight_left += sensors["sensor_left"]["distance"]
        else:                                                                                                       #Le robot est un robot allie
            weight_left -= (1 +  sensors["sensor_left"]["distance"])

    if sensors["sensor_back_left"]["isRobot"] == True:                                                              #Le sensor detecte un robot
        if sensors["sensor_back_left"]["isSameTeam"] == False and sensors["sensor_back_left"]["distance"] < 1:      #Le robot est un robot ennemie
            weight_left += sensors["sensor_back_left"]["distance"]
        else:                                                                                                       #Le robot est un robot allie
            weight_left -= (1 +  sensors["sensor_back_left"]["distance"])

    ################ RIGHT SIDE

    if sensors["sensor_front_right"]["isRobot"] == True:                                                            #Le sensor detecte un robot
        if sensors["sensor_front_right"]["isSameTeam"] == False and sensors["sensor_front_right"]["distance"] < 1:  #Le robot est un robot ennemie
            weight_right += sensors["sensor_front_right"]["distance"]
        else:                                                                                                       #Le robot est un robot allie
            weight_right -= (1 +  sensors["sensor_front_right"]["distance"])

    if sensors["sensor_right"]["isRobot"] == True:                                                                  #Le sensor detecte un robot
        if sensors["sensor_right"]["isSameTeam"] == False and sensors["sensor_right"]["distance"] < 1:              #Le robot est un robot ennemie
            weight_right += sensors["sensor_right"]["distance"]
        else:                                                                                                       #Le robot est un robot allie
            weight_right -= (1 +  sensors["sensor_right"]["distance"])

    if sensors["sensor_back_right"]["isRobot"] == True:                                                             #Le sensor detecte un robot
        if sensors["sensor_back_right"]["isSameTeam"] == False and sensors["sensor_back_right"]["distance"] < 1:    #Le robot est un robot ennemie
            weight_right += sensors["sensor_back_right"]["distance"]
        else:                                                                                                       #Le robot est un robot allie
            weight_right -= (1 +  sensors["sensor_back_right"]["distance"])  
    
    ################ BRAITENBERG 2EME REPULSIF -> MURS
    #### On débloque les robots coincés sur un mur

    if (sensors["sensor_front"]["isRobot"] == False and sensors["sensor_front"]["distance"] < 1):
        weight_right += 2
    elif (sensors["sensor_front_left"]["isRobot"] == False and sensors["sensor_front_left"]["distance"] < 1):
        weight_right += 2
    elif (sensors["sensor_front_right"]["isRobot"] == False and sensors["sensor_front_right"]["distance"] < 1):
        weight_left += 2

    ################ BRAITENBERG Ordre d'influence / de priorité sur les poids : MURS > ALLIE > ENNEMIE
    ################ MURs ajoute beaucoup de poids ; ALLIE enlève du poids ; ENNEMIE ajoute un peu de poids 

    if weight_left > weight_right:
        rotation -= 0.5
    elif weight_left < weight_right:
        rotation += 0.5 
    return translation, rotation

def step_genetique(robotId, sensors):

    global param

    translation = math.tanh ( param[0] + param[1] * sensors["sensor_front_left"]["distance"] + param[2] * sensors["sensor_front"]["distance"] + param[3] * sensors["sensor_front_right"]["distance"] + (param[8] * sensors["sensor_front_left"]["distance"])/2 + (param[9] * sensors["sensor_front"]["distance"])/2 + (param[10] * sensors["sensor_front_right"]["distance"])/2)
    rotation = math.tanh ( param[4] + param[5] * sensors["sensor_front_left"]["distance"] + param[6] * sensors["sensor_front"]["distance"] + param[7] * sensors["sensor_front_right"]["distance"] + (param[11] * sensors["sensor_front_left"]["distance"])/2 + (param[12] * sensors["sensor_front"]["distance"])/2 + (param[13] * sensors["sensor_front_right"]["distance"])/2 )

    return translation, rotation


def step(robotId, sensors) : 

    for _, v in sensors.items():
        if v['isRobot'] == True :
            
            return step_braitenberg(robotId, sensors)
    
    return step_genetique(robotId, sensors)


