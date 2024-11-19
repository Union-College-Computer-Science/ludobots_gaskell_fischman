import pybullet as p
from sensor import SENSOR
import pyrosim.pyrosim as pyrosim
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT():

   def __init__(self):
      self.motors = {}
      self.robotID = p.loadURDF("body.urdf")
      self.nn = NEURAL_NETWORK("brain.nndf")

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

   def Act(self):
      Angles = []
      for neuronName in self.nn.Get_Neuron_Names():
         if self.nn.Is_Motor_Neuron(neuronName):
            jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
            desiredAngle = self.nn.Get_Value_Of(neuronName)
            self.motors[jointName].setValue(desiredAngle, self.robotID)
            Angles.append(desiredAngle)
      return Angles

   def Think(self):
      self.nn.Update()
      # self.nn.Print()
