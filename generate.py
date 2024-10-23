import pyrosim.pyrosim as pyrosim

# pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])
# pyrosim.Send_Cube(name='Box2', pos=[0,2,2], size =[1,1,1])
# pyrosim.Send_Cube(name='Box3', pos=[0,1,1], size =[1,1,1])
# pyrosim.Send_Cube(name='Box4', pos=[0,4,4], size =[5,5,5])

# x = 1
# for j in range(5):
#     y = 1
#     x +=1
#     for k in range(5):
#         y+=1
#         z = .5
#         dim = 1 
#         for i in range(10):
#             pyrosim.Send_Cube(name="Box" + str([x,y,z]), pos=[x,y,z] , size=[dim, dim, dim])
#             z += 1
#             dim *= .9

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[0,4,0.5] , size=[1,1,1])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    # Link0 = pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[1,1,1])
    # Link0_Link1 = pyrosim.Send_Joint(name = "Link0_Link1" , parent= "Torso" , child = "Leg1" , type = "revolute", position = [0,0,1.5])
    # Link1 = pyrosim.Send_Cube(name="Leg1", size = [1,1,1])
    # Link1_Link2 = pyrosim.Send_Joint(name = "Link1_Link2" , parent= "Leg1" , child = "Leg2" , type = "revolute", position = [0,0,1])
    # Link2 = pyrosim.Send_Cube(name="Leg2", size = [1,1,1])
    # Link2_Link3 = pyrosim.Send_Joint(name = "Link2_Link3" , parent= "Leg2" , child = "Leg3" , type = "revolute", position = [1,0,0])
    # Link3 = pyrosim.Send_Cube(name="Leg3", size = [1,1,1])
    # Link3_Link4 = pyrosim.Send_Joint(name = "Link3_Link4" , parent= "Leg3" , child = "Leg4" , type = "revolute", position = [1,0,0])
    # Link4 = pyrosim.Send_Cube(name="Leg4", size = [1,1,1])
    # Link4_Link5 = pyrosim.Send_Joint(name = "Link4_Link5" , parent= "Leg4" , child = "Leg5" , type = "revolute", position = [0,0,-1])
    # Link5 = pyrosim.Send_Cube(name="Leg5", size = [1,1,1])
    # Link5_Link6 = pyrosim.Send_Joint(name = "Link5_Link6" , parent= "Leg5" , child = "Leg6" , type = "revolute", position = [0,0,-1])
    # Link6 = pyrosim.Send_Cube(name="Leg6", size = [1,1,1])

    Link1 = pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[1,1,1])
    Link1_Link2 = pyrosim.Send_Joint(name = "Link1_Link2" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,0.5])
    Link2 = pyrosim.Send_Cube(name="BackLeg", size=[1,1,1])
    Link2_Link3 = pyrosim.Send_Joint(name = "Link2_Link3" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [-1,0,0.5])
    Link3 = pyrosim.Send_Cube(name="FrontLeg", size=[1,1,1])

    pyrosim.End()

Create_World()
Create_Robot()
