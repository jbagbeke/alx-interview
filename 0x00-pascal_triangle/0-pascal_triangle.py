#!/usr/bin/python3
"""
    Pascal Triangle Generation Function
                                        """


def pascal_triangle(number):
    """
        Generates levels of pascal's triangle based on number provided
                                                                    """
    myArray = []
    masterArray = []

    for i in range(number):
        if len(myArray) == 0:
            myArray.append(1)
        else:
            tmp = []
            for j in range(len(myArray)):
                if j == 0:
                    tmp.append(myArray[j])
                if j + 1 >= len(myArray):
                    tmp.append(1)
                else:
                    tmp.append(myArray[j] + myArray[j + 1])
            myArray = tmp
        masterArray.append(myArray)

    return masterArray
