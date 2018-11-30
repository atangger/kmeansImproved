import numpy as np 
import math

ccenter1 = np.array([1.0,1.0])
ridus1 = 2.0
ccenter2 = np.array([1.0,1.0])
ridus2 = 20.0

pointnum = 100
fo = open("dataCircle.txt","w")
for i in range(pointnum):
    randAngle = np.random.uniform(0.0,2*math.pi)
    shuff = ridus1 * np.array([math.cos(randAngle),math.sin(randAngle)])
    fo.write("%f %f\n"%(shuff[0],shuff[1]))

for i in range(pointnum):
    randAngle = np.random.uniform(0.0,2*math.pi)
    shuff = ridus2 * np.array([math.cos(randAngle),math.sin(randAngle)])
    fo.write("%f %f\n"%(shuff[0],shuff[1]))