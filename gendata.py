import numpy as np 

ccenter1 = np.array([1.0,1.0])
ccenter2 = np.array([10.0,10.0])
pointnum = 20
fo = open("data.txt","w")
for i in range(pointnum):
    shuff = np.random.rand(1,2) + ccenter2
    fo.write("%f %f\n"%(shuff[0][0],shuff[0][1]))

for i in range(pointnum):
    shuff = np.random.rand(1,2) + ccenter1
    fo.write("%f %f\n"%(shuff[0][0],shuff[0][1]))