from numpy import *

def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split(' ')
        print(curLine)
        fltLine = [float(curLine[0]),float(curLine[1])]
        dataMat.append(fltLine)
    return dataMat
    
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

def randCent(dataSet, k):
    n = shape(dataSet)[0]
    nums = 0
    records = [0]*n
    centeroids = []
    while(nums < k):
        print(nums)
        randid = random.randint(0,n)
        while(records[randid] == 1):
            randid = random.randint(0,n)
        records[randid] = 1
        centeroids.append([dataSet[randid][0],dataSet[randid][1]])
        nums+=1
    centeroids = array(centeroids)
    return centeroids
    
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    n = shape(dataSet)[0]
    clusterAssment = [0]*n                
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(n):
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i] != minIndex: 
                clusterChanged = True
            clusterAssment[i] = minIndex

        for cent in range(k):
           mean = array([0.0,0.0])
           nums = 0
           for i in range(n):
                if(clusterAssment[i] == cent):
                    mean += dataSet[i,:]
                    nums +=1
           mean = (1/nums)*mean
           centroids[cent,:] = mean
    return centroids, clusterAssment
    
def show(dataSet, k, centroids, clusterAssment):
    from matplotlib import pyplot as plt  
    numSamples = dataSet.shape[0]  
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']  
    for i in range(numSamples):  
        markIndex = int(clusterAssment[i])  
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])  
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']  
    for i in range(k):  
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)  
    plt.show()
      
def main():
    dataMat = array(loadDataSet('data.txt'))
    myCentroids, clustAssing = kMeans(dataMat,4)
    rint(myCentroids)
    show(dataMat, 4, myCentroids, clustAssing)  
    
    
if __name__ == '__main__':
    main()