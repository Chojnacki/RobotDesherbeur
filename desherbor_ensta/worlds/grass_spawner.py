#!/usr/bin/env python

import rospy
from gazebo_msgs.srv import SpawnModel, SpawnModelRequest
import random
from time import sleep

rospy.init_node("grass_spawner")

file_path = rospy.get_param("/grass_spawner/chemin")
NbHerbe = rospy.get_param("/grass_spawner/NbHerbe")

f = open(file_path, "r")
strdebase = "<radius>0.2</radius>"

filesdf = f.read()

rospy.wait_for_service('/gazebo/spawn_sdf_model')

gazeboSpawnModel = rospy.ServiceProxy("/gazebo/spawn_sdf_model", SpawnModel)

for i in range(NbHerbe):
    x = 10 * random.random() -5
    y = 10 * random.random()- 5
    rayon = 0.06*random.random() + 0.01
    strtochange = "<radius>"+str(rayon)+"</radius>"
    filesdf = filesdf.replace(strdebase,strtochange)
    strdebase = strtochange
    request = SpawnModelRequest()
    request.model_name = "Grass"+str(i)
    request.model_xml = filesdf
    request.robot_namespace = "Herbe"+str(i)
    request.initial_pose.position.x = x
    request.initial_pose.position.y = y
    request.initial_pose.position.z = 0
    request.initial_pose.orientation.x = 0
    request.initial_pose.orientation.y = 0
    request.initial_pose.orientation.z = 0
    request.initial_pose.orientation.w = 1.0
    response = gazeboSpawnModel(request)

#rossrv info SpawnModel