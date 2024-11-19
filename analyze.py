import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use('ggplot')

backLegSensorValues = np.load(os.path.join(os.getcwd() , "data/backLegSensor.npy"))
frontLegSensorValues = np.load(os.path.join(os.getcwd() , "data/frontLegSensor.npy"))
FrontLeg_TargetAngles = np.load(os.path.join(os.getcwd() , "data/frontLegAngles.npy"))
BackLeg_TargetAngles = np.load(os.path.join(os.getcwd() , "data/backLegAngles.npy"))

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
plt.show()