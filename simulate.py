import pybullet as p
import time, pybullet_data, random
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()

backLegSensorValues = np.zeros(c.iters)
frontLegSensorValues = np.zeros(c.iters)

sin_vec = np.linspace(np.pi, -np.pi, c.iters)

FrontLeg_TargetAngles = [c.FrontLeg_amplitude * np.sin(c.FrontLeg_frequency * i + c.FrontLeg_phaseOffset) for i in sin_vec]

BackLeg_TargetAngles = [c.BackLeg_amplitude * np.sin(c.BackLeg_frequency * i + c.BackLeg_phaseOffset) for i in sin_vec]

np.save("data/frontLegAngles", FrontLeg_TargetAngles)
np.save("data/backLegAngles", BackLeg_TargetAngles)

np.save("data/backLegSensor", backLegSensorValues)
np.save("data/frontLegSensor", frontLegSensorValues)