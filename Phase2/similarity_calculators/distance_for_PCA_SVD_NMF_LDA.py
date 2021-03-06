# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:52:03 2020

@author: Jaysn
"""
from math import sqrt

# def dot(v1, v2):
#     return sum(x*y for x, y in zip(v1, v2))

# def length(v):
#     return sqrt(dot(v, v))

# def sim(v1, v2): 
#     return dot(v1, v2) / (length(v1) * length(v2))

def calculate_similarity(query, gesture_data):
    distance = 1
    for query_value, gesture_value in zip(query, gesture_data):
        distance += abs(query_value - gesture_value)
    return 1/distance

    # converted to cosine similarity because
    # k-means wasn't able to process infinity values
    # return abs(sim(query, gesture_data))
    # return -(sqrt(sum([(x-y)**2 for x,y in zip(query, gesture_data)])))
        