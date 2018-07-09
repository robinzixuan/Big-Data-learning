#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 09:28:27 2018

@author: luohaozheng
"""

#!/usr/bin/python
 # coding=utf-8
#########################################
# kNN: k Nearest Neighbors
 
 #  输入:      newInput:  (1xN)的待分类向量
 #             dataSet:   (NxM)的训练数据集
 #             labels:     训练数据集的类别标签向量
 #             k:         近邻数
 
 # 输出:     可能性最大的分类标签
 #########################################
 
import numpy as np
import operator
 
 # 创建一个数据集，包含2个类别共4个样本
def createDataSet():
    # 生成一个矩阵，每行表示一个样本
     group = np.array([[1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
     # 4个样本分别所属的类别
     labels = ['A', 'A', 'B', 'B']
     return group, labels
 
 # KNN分类算法函数定义
def kNNClassify(newInput, dataSet, labels, k):
     numSamples = dataSet.shape[0]   # shape[0]表示行数
     diff = np.tile(newInput, (numSamples, 1)) - dataSet  # 按元素求差值
     squaredDiff = diff ** 2  # 将差值平方
     squaredDist = sum(squaredDiff, axis = 1)   # 按行累加
     distance = squaredDist ** 0.5  # 将差值平方和求开方，即得距离
 
     # # step 2: 对距离排序
     # argsort() 返回排序后的索引值
     sortedDistIndices = np.argsort(distance)
     classCount = {} # define a dictionary (can be append element)
     for i in range(k):
         # # step 3: 选择k个最近邻
         voteLabel = labels[sortedDistIndices[i]]
         # # step 4: 计算k个最近邻中各类别出现的次数
         # when the key voteLabel is not in dictionary classCount, get()
         # will return 0
         classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
 
     # # step 5: 返回出现次数最多的类别标签
     maxCount = 0
     for key, value in classCount.items():
         if value > maxCount:
             maxCount = value
             maxIndex = key
     return maxIndex
 
def main():    
    # 生成数据集和类别标签
    dataSet, labels = createDataSet()
    # 定义一个未知类别的数据
    testX = np.array([1.2, 1.0])
    k = 3
    # 调用分类函数对未知数据分类
    outputLabel = kNNClassify(testX, dataSet, labels, k)
    print( "Your input is:", testX, "and classified to class: ", outputLabel) 
    testX = np.array([0.1, 0.3])
    outputLabel = kNNClassify(testX, dataSet, labels, k)
    print( "Your input is:", testX, "and classified to class: ", outputLabel)
    
main()