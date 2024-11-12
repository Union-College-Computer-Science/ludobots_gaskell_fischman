import pybullet as p
import time, pybullet_data, random
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()

# physicsClient = p.connect(p.GUI)

# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# p.setGravity(0,0,-9.8)

# planeID = p.loadURDF("plane.urdf")
# robotID = p.loadURDF("body.urdf")

# p.loadSDF("world.sdf")
# # testing new branch

# backLegSensorValues = np.zeros(c.iters)
# frontLegSensorValues = np.zeros(c.iters)

# sin_vec = np.linspace(np.pi, -np.pi, c.iters)

# FrontLeg_TargetAngles = [c.FrontLeg_amplitude * np.sin(c.FrontLeg_frequency * i + c.FrontLeg_phaseOffset) for i in sin_vec]

# BackLeg_TargetAngles = [c.BackLeg_amplitude * np.sin(c.BackLeg_frequency * i + c.BackLeg_phaseOffset) for i in sin_vec]

# np.save("data/frontLegAngles", FrontLeg_TargetAngles)
# np.save("data/backLegAngles", BackLeg_TargetAngles)

# pyrosim.Prepare_To_Simulate(robotID)
# for i in range(0, c.iters):
#     p.stepSimulation()

#     pos = (np.pi/2)*random.uniform(-1,1)

#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

#     pyrosim.Set_Motor_For_Joint(bodyIndex=robotID, jointName="Torso_BackLeg", controlMode =p.POSITION_CONTROL, targetPosition=BackLeg_TargetAngles[i], maxForce=50)

#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

#     pyrosim.Set_Motor_For_Joint(bodyIndex=robotID, jointName="Torso_FrontLeg", controlMode =p.POSITION_CONTROL, targetPosition=FrontLeg_TargetAngles[i], maxForce=50)

#     time.sleep(0.01)


# np.save("data/backLegSensor", backLegSensorValues)
# np.save("data/frontLegSensor", frontLegSensorValues)

# p.disconnect()


