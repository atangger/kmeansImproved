import numpy as np 
import math

ccenter1 = np.array([1.0,1.0])
ridus1 = 2.0
ccenter2 = np.array([1.0,1.0])
ridus2 = 20.0

pointnum = 100
rotatAngle = -0.2 * math.pi

offset = np.array([-20,10])

rotMat = np.array([[math.cos(rotatAngle),-math.sin(rotatAngle)],
                   [math.sin(rotatAngle),math.cos(rotatAngle)]])

fo = open("dataElips.txt","w")
for i in range(pointnum):
    randAngle = np.random.uniform(0.0,2*math.pi)
    randRidus = np.random.uniform(0.0,ridus1)
    shuff =np.matmul(rotMat,np.array([3 * randRidus *math.cos(randAngle),30 * randRidus *math.sin(randAngle)]))
    fo.write("%f %f\n"%(shuff[0],shuff[1]))

for i in range(pointnum):
    randAngle = np.random.uniform(0.0,2*math.pi)
    randRidus = np.random.uniform(0.0,ridus1)
    shuff =np.matmul(rotMat,np.array([3 * randRidus *math.cos(randAngle),30 * randRidus *math.sin(randAngle)])) + offset
    fo.write("%f %f\n"%(shuff[0],shuff[1]))
