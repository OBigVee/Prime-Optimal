#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:35:17 2020

@author: obigvee
"""
import matplotlib.pyplot as plt
from  robotClass import robot
from helpers import displayWorld


'''
define a small 10x10 square world,
a measurement range that is half 
that of the world and small values
for motion and measurement noise. 
'''


world_size         = 10.0    # size of world (square)
measurement_range  = 5.0     # range at which we can sense landmarks
motion_noise       = 0.2      # noise in robot motion
measurement_noise  = 0.2      # noise in the measurements

# instantiate a robot, r
r = robot(world_size, measurement_range, motion_noise, measurement_noise)

# print out the location of r
print("initial coordinate  is:".title())
print(r)

print("==============================================")

# define figure size
plt.rcParams["figure.figsize"] = (5,5)

# call display_world and display the robot in it's grid world
print(r)
displayWorld(int(world_size), [r.x, r.y])

# choose values of dx and dy (negative works, too)
dx = 1
dy = 2
r.move(dx, dy)

# print out the exact location
print(r)

# display the world after movement, not that this is the same call as before
# the robot tracks its own movement
displayWorld(int(world_size), [r.x, r.y])



"""
The robot class has a function make_landmarks which randomly generates locations for 
the number of specified landmarks
"""

# create any number of landmarks
num_landmarks = 7
r.make_landmarks(num_landmarks)

# print out our robot's exact location
print(r)

# display the world including these landmarks

displayWorld(int(world_size), [r.x, r.y], r.landmarks)

# print the locations of the landmarks
print('Landmark locations [x,y]: ', r.landmarks)

print("Sensing around".upper())
# try to sense any surrounding landmarks
measurements = r.sense()
#display_world(int(world_size), [r.x, r.y], r.landmarks)
# this will print out an empty list if `sense` has not been implemented
for measure in measurements:
    print(str(measure)+'\n')
    
    
## Data
data = []

# after a robot first senses, then moves (one time step)
# that data is appended like so:
data.append([measurements, [dx, dy]])

# for our example movement and measurement
print("printing Data...".upper())
print(data)

time_step = 0

#access robot measurements:
print("printing measurements".upper())
print('Measurements: ',data[time_step][0])
print('\n')
# and its motion for a given time step:
print('Motion: ', data[time_step][1])
