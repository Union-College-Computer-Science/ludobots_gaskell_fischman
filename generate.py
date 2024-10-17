import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

# pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])
# pyrosim.Send_Cube(name='Box2', pos=[0,2,2], size =[1,1,1])
# pyrosim.Send_Cube(name='Box3', pos=[0,1,1], size =[1,1,1])
# pyrosim.Send_Cube(name='Box4', pos=[0,4,4], size =[5,5,5])

x = 1
for j in range(5):
    y = 1
    x +=1
    for k in range(5):
        y+=1
        z = .5
        dim = 1 
        for i in range(10):
            pyrosim.Send_Cube(name="Box" + str([x,y,z]), pos=[x,y,z] , size=[dim, dim, dim])
            z += 1
            dim *= .9

pyrosim.End()

