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

  def run(self):
    for i in range(0, c.iters):
      p.stepSimulation()
      time.sleep(0.01)
      self.robot.Sense(i)


  def __del__(self):
    p.disconnect()