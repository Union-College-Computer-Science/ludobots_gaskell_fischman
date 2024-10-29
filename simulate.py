import pybullet as p
import time, pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

backLegSensorValues = np.zeros(10000)

pyrosim.Prepare_To_Simulate(robotID)
for i in range(0, 10000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    time.sleep(0.001)

    
np.save("data/backLegSensor", backLegSensorValues)

p.disconnect()

