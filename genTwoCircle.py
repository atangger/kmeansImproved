import numpy as np 
import math

ccenter1 = np.array([0,0])
ridus1 = 10.0
ccenter2 = np.array([5.0,-2])
ridus2 = 10.0

pointnum = 200
fo = open("dataTwoCircle.txt","w")
for i in range(pointnum):
    randAngle = np.random.uniform(math.pi,2*math.pi)
    shuff = ridus1 * np.array([math.cos(randAngle),math.sin(randAngle)]) + ccenter1
    fo.write("%f %f\n"%(shuff[0],shuff[1]))

for i in range(pointnum):
    randAngle = np.random.uniform(0.0,math.pi)
    shuff = ridus2 * np.array([math.cos(randAngle),math.sin(randAngle)]) + ccenter2
    fo.write("%f %f\n"%(shuff[0],shuff[1]))