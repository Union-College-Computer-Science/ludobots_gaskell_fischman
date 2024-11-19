# Ludobots

This project follows rhe ludobots tutorial as outlined [here]([https://www.reddit.com/r/ludobots/wiki/hillclimber/)

The project uses the pyrogym simulation environment to create a robot that can evolve to exhibit improved gaits. The brief for this project was to complete up to part K - as such our robot shows signs of locomotion and uses neural networks based on a random seed to cause movement.

## Running the project

The user has two choices when running the project.

1. Run generate.py followed by simulate.py
   - generate.py creates the initial conditions for the world and robot
   - simulate.py runs a single 10k timestep simulation of the robot created

2. Run search.py
   - This script automates generate.py and simulate.py into a single executable
   - search.py creates two simulations to show how the different randomized seed values cause different behaviors in the robot
