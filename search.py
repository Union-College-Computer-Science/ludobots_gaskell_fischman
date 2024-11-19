import os

num_execs = 2

for x in range(0,num_execs):
    os.system("python3 generate.py")
    os.system("python3 simulate.py")
