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

   def setValue(self, desiredAngle, robotID):
      pyrosim.Set_Motor_For_Joint(bodyIndex=robotID, jointName=self.jointName, controlMode=p.POSITION_CONTROL, targetPosition=desiredAngle, maxForce=50)
