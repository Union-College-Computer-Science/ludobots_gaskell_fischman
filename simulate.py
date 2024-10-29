import pybullet as p
import time, pybullet_data, random
import pyrosim.pyrosim as pyrosim
import numpy as np

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

iters = 1000

backLegSensorValues = np.zeros(iters)
frontLegSensorValues = np.zeros(iters)

amplitude = np.pi/4
frequency = 1
phaseOffset = 0

targetAngles = amplitude * np.sin(np.linspace(np.pi, -np.pi, (frequency * iters) + phaseOffset))

np.save("data/targetAngles", targetAngles)

pyrosim.Prepare_To_Simulate(robotID)
for i in range(0, iters):
    p.stepSimulation()

    pos = (np.pi/2)*random.uniform(-1,1)

    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

    pyrosim.Set_Motor_For_Joint(bodyIndex=robotID, jointName="Torso_BackLeg", controlMode =p.POSITION_CONTROL, targetPosition=targetAngles[i], maxForce=50)

    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(bodyIndex=robotID, jointName="Torso_FrontLeg", controlMode =p.POSITION_CONTROL, targetPosition=targetAngles[i], maxForce=50)

    time.sleep(0.001)


np.save("data/backLegSensor", backLegSensorValues)
np.save("data/frontLegSensor", frontLegSensorValues)

p.disconnect()


