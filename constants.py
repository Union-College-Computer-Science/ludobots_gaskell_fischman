import numpy as np

iters = 1000

backLegSensorValues = np.zeros(iters)
frontLegSensorValues = np.zeros(iters)

sin_vec = np.linspace(np.pi, -np.pi, iters)

FrontLeg_amplitude = np.pi/4
FrontLeg_frequency = 5
FrontLeg_phaseOffset = 0

FrontLeg_TargetAngles = [FrontLeg_amplitude * np.sin(FrontLeg_frequency * i + FrontLeg_phaseOffset) for i in sin_vec]

BackLeg_amplitude = np.pi/4
BackLeg_frequency = 5
BackLeg_phaseOffset = 1

BackLeg_TargetAngles = [BackLeg_amplitude * np.sin(BackLeg_frequency * i + BackLeg_phaseOffset) for i in sin_vec]