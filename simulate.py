import pybullet as p
import time, pybullet_data

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

for i in range(0, 100000000000):
    p.stepSimulation()
    time.sleep(0.001)
    print(i)

p.disconnect()

