import pybullet_data
from world import WORLD
from robot import ROBOT
import pybullet as p
import numpy as np
import constants as c
import time, random
import pyrosim.pyrosim as pyrosim


class SIMULATION():
  def __init__(self):

    self.physicsClient = p.connect(p.GUI)

    p.setAdditionalSearchPath(pybullet_data.getDataPath())

    p.setGravity(0,0,-9.8)

    self.world = WORLD()
    self.robot = ROBOT()

    pyrosim.Prepare_To_Simulate(self.robot.robotID)

    self.robot.Prepare_To_Sense()
    self.robot.Prepare_To_Act() #DAMN

  def run(self):
    Angles_BackLeg = []
    Angles_FrontLeg = []
    for i in range(0, c.iters):
      p.stepSimulation()

      self.robot.Sense(i)

      self.robot.Think()
      
      Angles = self.robot.Act()
      Angles_BackLeg.append(Angles[0])
      Angles_FrontLeg.append(Angles[0])

      time.sleep(0.1)

    np.save("data/PartK/backLegSensor", self.robot.sensors['BackLeg'].values)
    np.save("data/PartK/frontLegSensor", self.robot.sensors['FrontLeg'].values)

    np.save("data/PartK/backLegMotorValues", Angles_BackLeg)
    np.save("data/PartK/frontLegMotorValues", Angles_FrontLeg)

  def __del__(self):
    p.disconnect()