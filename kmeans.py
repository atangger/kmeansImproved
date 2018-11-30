from numpy import *

def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split(' ')
        print(curLine)
        fltLine = [float(x) for x in curLine]
        print(fltLine)
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
        print("in randCent")
        flagMult = False
        for i in range(len(centeroids)):
            if distEclud(dataSet[randid],centeroids[i]) == 0:
                flagMult =True
        if not flagMult:
            centeroids.append(dataSet[randid])
            nums+=1
    centeroids = array(centeroids)
    return centeroids
    
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    n = shape(dataSet)[0]
    print("NOW dataset = ")
    print(dataSet)
    clusterAssment = [0]*n                
    centroids = createCent(dataSet, k)
    print("init center:")
    print(centroids)
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
           mean = zeros(shape(dataSet)[1])
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
    plt.figure(1)
    numSamples = dataSet.shape[0]  
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']  
    for i in range(numSamples):  
        markIndex = int(clusterAssment[i])  
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])  
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']  
    for i in range(k):  
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)  
    plt.show()

def showOnlyPoints(dataSet, k, clusterAssment):
    from matplotlib import pyplot as plt  
    plt.figure(2)
    numSamples = dataSet.shape[0]  
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']  
    for i in range(numSamples):  
        markIndex = int(clusterAssment[i])  
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])  
    plt.show()
      
def main():
    k = 3
    dataMat = array(loadDataSet('data.txt'))
    dataTransformed = array(loadDataSet('transformed.txt'))
    # print(dataTransformed)
    # myCentroids, clustAssing = kMeans(dataMat,k)
    transedMyCenterIds, transedClustAssing = kMeans(dataTransformed,k)
    # show(dataMat,k,myCentroids,clustAssing)
    showOnlyPoints(dataMat, k, transedClustAssing)  
    
    
if __name__ == '__main__':
    main()