import pybullet as p
import time, pybullet_data, random
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from simulation import SIMULATION


simulation = SIMULATION()

for i in range(0, c.iters):

    p.stepSimulation()

    time.sleep(0.01)

del simulation