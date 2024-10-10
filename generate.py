import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])
pyrosim.Send_Cube(name='Box2', pos=[0,2,2], size =[1,1,1])
pyrosim.Send_Cube(name='Box3', pos=[0,1,1], size =[1,1,1])
pyrosim.Send_Cube(name='Box4', pos=[0,4,4], size =[5,5,5])

pyrosim.End()

