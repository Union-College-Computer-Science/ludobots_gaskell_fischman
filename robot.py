import pybullet as p
from sensor import SENSOR
import pyrosim.pyrosim as pyrosim
from motor import MOTOR

class ROBOT():

   def __init__(self):
      self.motors = {}
      self.robotID = p.loadURDF("body.urdf")

   def Prepare_To_Sense(self):
      self.sensors = {}
      for linkName in pyrosim.linkNamesToIndices:
         self.sensors[linkName] = SENSOR(linkName)

   def Sense(self, index):
      for linkName in self.sensors:
         self.sensors[linkName].Get_Value(index)

   def Prepare_To_Act(self):
      self.motors = {}
      for jointName in pyrosim.jointNamesToIndices:
         self.motors[jointName] = MOTOR(jointName)

   def Act(self, index):
      for jointName in self.motors:
         self.motors[jointName].setValue(index, self.robotID)
