import pybullet as p
import time, pybullet_data
import pyrosim.pyrosim as pyrosim

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotID)
for i in range(0, 100000000000):
    p.stepSimulation()
    print(pyrosim.linkNamesToIndices)
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    time.sleep(0.001)
    print(i)

p.disconnect()

