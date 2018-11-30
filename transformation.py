import numpy as np
from sklearn .neighbors import NearestNeighbors

np.set_printoptions(threshold=np.nan,linewidth = 100)

def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split(' ')
        fltLine = [float(curLine[0]),float(curLine[1])]
        dataMat.append(fltLine)
    return dataMat 

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

def main():
    dataMat = np.array(loadDataSet('dataCircle.txt'))
    transformedData = transform(dataMat,5,2)


def findGraph(dataset,r):
    n = dataset.shape[0]
    nbrs = NearestNeighbors(n_neighbors=r+1, algorithm='ball_tree').fit(dataset)
    graph = nbrs.kneighbors_graph(dataset).toarray()
    print("graph")
    print(graph)
    W = np.identity(graph.shape[0])
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                W[i,j] = 1
                W[j,i] = 1
    print("W")
    print(W)
    D = np.zeros(graph.shape)
    for i in range(n):
        D[i][i] = np.sum(W[i,:])
    return D,W

def transform(dataset,r,k):
    D,W = findGraph(dataset,r)
    L = D - W   
    eigenValues, eigenVectors = np.linalg.eig(L)
    idx = eigenValues.argsort()[::1]   
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:,idx]
    print(eigenValues)
    kthEigeVecs = eigenVectors[:,0:k]
    print(kthEigeVecs[:,0:k])
    print(idx)
    of = open("transformedCircle.txt","w")
    for i in range(kthEigeVecs.shape[0]):
        for j in range(kthEigeVecs.shape[1]):
            of.write("%f "%(kthEigeVecs[i,j]))
        of.write("\n")
    print(kthEigeVecs[0,:])

if __name__ == '__main__':
    main()

