import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim

class SENSOR():

   def __init__(self, linkName):
      self.linkName = linkName
      self.values = np.zeros(c.iters)

   def Get_Value(self, index):
         self.values[index] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)