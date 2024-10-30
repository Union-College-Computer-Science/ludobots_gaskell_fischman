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
# testing new branch
iters = 1000

backLegSensorValues = np.zeros(iters)
frontLegSensorValues = np.zeros(iters)

sin_vec = np.linspace(np.pi, -np.pi, iters)

FrontLeg_amplitude = np.pi/4
FrontLeg_frequency = 5
FrontLeg_phaseOffset = 0

FrontLeg_TargetAngles = [FrontLeg_amplitude * np.sin(FrontLeg_frequency * i + FrontLeg_phaseOffset) for i in sin_vec]

BackLeg_amplitude = np.pi/4
BackLeg_frequency = 5
BackLeg_phaseOffset = 1

BackLeg_TargetAngles = [BackLeg_amplitude * np.sin(BackLeg_frequency * i + BackLeg_phaseOffset) for i in sin_vec]

np.save("data/frontLegAngles", FrontLeg_TargetAngles)
np.save("data/backLegAngles", BackLeg_TargetAngles)

pyrosim.Prepare_To_Simulate(robotID)
for i in range(0, iters):
    p.stepSimulation()

    pos = (np.pi/2)*random.uniform(-1,1)

    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

    pyrosim.Set_Motor_For_Joint(bodyIndex=robotID, jointName="Torso_BackLeg", controlMode =p.POSITION_CONTROL, targetPosition=BackLeg_TargetAngles[i], maxForce=50)

    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(bodyIndex=robotID, jointName="Torso_FrontLeg", controlMode =p.POSITION_CONTROL, targetPosition=FrontLeg_TargetAngles[i], maxForce=50)

    time.sleep(0.01)


np.save("data/backLegSensor", backLegSensorValues)
np.save("data/frontLegSensor", frontLegSensorValues)

p.disconnect()


