import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np
import pybullet as p

class MOTOR():
   
   def __init__(self, jointName):
      self.jointName = jointName
      self.frequency = c.frequency
      self.amplitude = c.amplitude
      self.phaseOffset = c.phaseOffset

      self.TargetAngles = [self.amplitude * np.sin(self.frequency * i + self.phaseOffset) for i in c.sin_vec]

   def setValue(self, index, robotID):
      pyrosim.Set_Motor_For_Joint(bodyIndex=robotID, jointName=self.jointName, controlMode=p.POSITION_CONTROL, targetPosition=self.TargetAngles[index], maxForce=50)
