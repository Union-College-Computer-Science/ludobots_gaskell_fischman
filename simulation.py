import pybullet_data
from world import WORLD
from robot import ROBOT
import pybullet as p
import numpy as np
import constants as c
import time, random
import pyrosim.pyrosim as pyrosim


class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()

        self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)
        pyrosim.Prepare_To_Simulate(self.robot.robotID)

    def run(self):
      for i in range(0, c.iters):
        print(i)
            # p.stepSimulation()

            # pos = (np.pi/2)*random.uniform(-1,1)

            # c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

            # pyrosim.Set_Motor_For_Joint(bodyIndex=self.robot.robotID, jointName="Torso_BackLeg", controlMode =p.POSITION_CONTROL, targetPosition=c.BackLeg_TargetAngles[i], maxForce=50)

            # c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

            # pyrosim.Set_Motor_For_Joint(bodyIndex=self.robot.robotID, jointName="Torso_FrontLeg", controlMode =p.POSITION_CONTROL, targetPosition=c.FrontLeg_TargetAngles[i], maxForce=50)

            # time.sleep(0.01)
    
    def __del__(self):
       p.disconnect()
       self.physicsClient.disconnect()