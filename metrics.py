import math
import sys

def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    if len(data) == 0:
        return []
    total: float = 0
    for integer in data:
        total = total + integer
    return round(total / len(data), 2)


def maximum(data: list) -> float:
    """
    Calculate maximum value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the maximum of this list
    """
    if len(data) == 0:
        return []
    maximum: float = (-1 * sys.maxsize) - 1;
    for num in data:
        if num > maximum:
            maximum = num
    return round(maximum, 2)


def variance(data: list) -> float:
    """
    Calculate variance value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the maximum of this list
    """
    if len(data) == 0:
        return []
    total: float = 0
    mean: float = average(data)
    for integer in data:
        total = total + ((integer - mean) ** 2)
    return round(total / float(len(data)), 2)
    


def standard_deviation(data: list) -> float:
    """
    Calculate variance value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the maximum of this list
    """
    if len(data) == 0:
        return []
    variance_num: float = variance(data)
    return round(math.sqrt(variance_num), 2)
