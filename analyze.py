import numpy as np
import matplotlib.pyplot as plt
import os

backLegSensorValues = np.load(os.path.join(os.getcwd() , "data/backLegSensor.npy")) # Check with John since we don't know if this ref is okay
frontLegSensorValues = np.load(os.path.join(os.getcwd() , "data/frontLegSensor.npy"))
targetAngles = np.load(os.path.join(os.getcwd() , "data/targetAngles.npy"))

plt.figure(1)
plt.plot(backLegSensorValues, color="r", linewidth=2, label="Back leg sensor values")
plt.plot(frontLegSensorValues, color="b", label="Front leg sensor values")
plt.ylim((-1.5,1.5))
plt.legend(loc="upper right")

plt.figure(2)
plt.plot(targetAngles, color="b", linewidth=1, label="Sinosoid target angles")
plt.ylim((-1,1))
plt.legend(loc="upper right")
plt.show()