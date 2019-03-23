#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from scipy.spatial import distance


class FMap:
    
    def __init__(self, num_dimension, n_points=2):
        self.num_dimension = num_dimension
        self.newDimension = []
        self.n_points = n_points

    def train(self,data):
        data = data.values
        dist_array = np.zeros((self.n_points, self.n_points), dtype = np.float)
        
        for i in range(self.n_points):
            for j in range(self.n_points):
                
                dist = distance.euclidean(data[i], data[j]) 
                dist_array[i-1][j-1] = dist
                dist_array[j-1][i-1] = dist
        
        self.fastMap(self.num_dimension, dist_array)
    
    def farthest_point(self,distance):
        
        obj_a = np.random.randint(0,9)
        while True: 
            farthest = max(distance[obj_a])
            obj_b = distance[obj_a].index(farthest)
            tmpDistance = max(distance[obj_b])
            tmpObj = distance[obj_b].index(tmpDistance)
            if (tmpObj == obj_a):
                break
            else:
                obj_a = obj_b
            
        if obj_a < obj_b:
            return (obj_a, obj_b)
        else:
            return (obj_b, obj_a)
      
      
    def fastMap(self, n, distance):
        if n<=0:
            return
        distance = distance.tolist()
        pivots = self.farthest_point(distance)
        
        a = pivots[0]
        b = pivots[1]
        farthest = distance[a][b]
        dimension = []
        
        for i in range(self.n_points):
            tmpDistance = 0
            if i == a:
                dimension.append(0)
            elif i == b:
                dimension.append(farthest)
            else:
                if farthest == 0:
                    dimension.append(0)
                else:
                    tmpDistance = ((distance[a][i]**2) + (farthest**2) - (distance[b][i]**2))/float(2 * farthest) 
                    dimension.append(tmpDistance)
        
        self.newDimension.append(dimension)
        projection = np.zeros((self.n_points, self.n_points), dtype = np.float)
        
        if n >= 1:
            for i in range (self.n_points):
                for j in range (self.n_points):
                    tmp = (distance[i][j] ** 2) - ((dimension[i] - dimension[j]) ** 2)
                    projection[i][j] = np.sqrt(tmp)
            self.fastMap(n-1, projection)
                  
# def main():
#     #readfile = r"C:\Users\amiya\Desktop\USC GRAD\Machine Learning\Assignment\HW3\fastmap-data.txt"
#     #nameFile = r"C:\Users\amiya\Desktop\USC GRAD\Machine Learning\Assignment\HW3\fastmap-wordlist.txt"
    
# #     readfile = sys.argv[1]
# #     nameFile = sys.argv[2]
    
# #     fd=open(nameFile,"r")
    
# #     name = fd.read()
# #     nameList = name.strip().split('\r\n')
    
# #     data = pd.read_csv(readfile, sep = '\t', header = None)
# #     data = dictionary['LBP'][0]
# #     print(data.values)
    
# #     num_dimension = 2
    
# #     FastMap = FMap(num_dimension, n_points=len(data))
# #     FastMap.train(data)
    
# #     print(num_dimension)
    
# #     newDimension1 = np.array(FastMap.newDimension)
# #     newDimension1=newDimension1.T
    
# #     print(newDimension1)

   
# #     fig,ax = plt.subplots()
    
# #     ax.scatter(newDimension1[:,0], newDimension1[:,1])
    
# #     for i, txt in enumerate(nameList):
# #         ax.annotate(txt, (newDimension1[i][0], newDimension1[i][1]))
        
# #     plt.show()

# # if __name__ == '__main__':
# #     main() 


# # In[32]:


# # data = dictionary['LBP'][0]
# # data

