import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use('ggplot')

backLegSensorValues = np.load(os.path.join(os.getcwd() , "data/backLegSensor.npy"))
frontLegSensorValues = np.load(os.path.join(os.getcwd() , "data/frontLegSensor.npy"))
FrontLeg_TargetAngles = np.load(os.path.join(os.getcwd() , "data/frontLegAngles.npy"))
BackLeg_TargetAngles = np.load(os.path.join(os.getcwd() , "data/backLegAngles.npy"))

FrontLeg_Sensor_K = np.load(os.path.join(os.getcwd() , "data/PartK/backLegSensor.npy"))
BackLeg_Sensor_K = np.load(os.path.join(os.getcwd() , "data/PartK/backLegSensor.npy"))
FrontLeg_Angles_K = np.load(os.path.join(os.getcwd() , "data/PartK/backLegMotorValues.npy"))
BackLeg_Angles_K = np.load(os.path.join(os.getcwd() , "data/PartK/backLegMotorValues.npy"))


plt.figure(1)
plt.plot(backLegSensorValues, linewidth=3, label="Back leg sensor values")
plt.plot(frontLegSensorValues, label="Front leg sensor values")
plt.ylim((-1.5,1.5))
plt.legend(loc="upper right")

plt.figure(2)
plt.plot(FrontLeg_TargetAngles, linewidth=3, label="Front Leg target angles")
plt.plot(BackLeg_TargetAngles, linewidth=1, label="Back Leg target angles")
plt.ylim((-1,1))
plt.legend(loc="upper right")

plt.figure(3)
plt.plot(FrontLeg_Sensor_K, linewidth=3, label="Front Leg sensor values Final (part K)")
plt.plot(BackLeg_Sensor_K, linewidth=1, label="Back Leg sensor values Final (part K)")
plt.legend(loc="upper right")

plt.figure(4)
plt.plot(FrontLeg_Angles_K, linewidth=3, label="Front Leg motor values Final (part K)")
plt.plot(BackLeg_Angles_K, linewidth=1, label="Back Leg motor values Final (part K)")
plt.legend(loc="upper right")
plt.show()