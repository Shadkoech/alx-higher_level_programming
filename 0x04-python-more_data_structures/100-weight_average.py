#!/usr/bin/python3

def weight_average(my_list=[]):
    """function returning a weighted average of an integer
    Weighted Average = (Sum of (Score * Weight)) / (Sum of Weights)
    """

    total_score = 0
    total_weight = 0

    if len(my_list) == 0:
        return 0

    for tple in my_list:
        total_score += tple[0] * tple[1]
        total_weight += tple[1]

    return (total_score / total_weight)
