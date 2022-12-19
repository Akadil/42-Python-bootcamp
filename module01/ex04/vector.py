# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/06 19:30:08 by akalimol          #+#    #+#              #
#    Updated: 2022/12/19 15:56:50 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Vector:
    """
        My own vector
    """
    def __init__(self, values, shape):
        
        # Check for correctness of the 'values'

        ## Check values. Check its type 
        if type(values) is not list:
            print(f'{values} is not a list')
            sys.exit()

        ## Check if it is row
        if len(values) == 1:
            for element in values[0]:
                if type(element) is not float:
                    print(f'The element {element} is not float')
                    sys.exit()
        ## check if it is column
        else:
            for element in values:
                if len(element) != 1 and type(element[0]) is not float:
                    print(f'The element {element} is not float or contain more than one float in it')
                    sys.exit()
        self.values = values

        # Check for the correctness of the shape
        if type(shape) is not tuple:
            print(f'{shape} is not a tuple')
            sys.exit()
        if len(shape) != 2:
            print("The wrong shape of 'shape'")
            sys.exit()
        if shape[0] != 1 or shape[1] != 1:
            print("You have to give me vector, not matrix")
            sys.exit()
        self.shape = shape

    def __add__(self, vec2):

        # Check the shapes of the vectors
        if self.shape != vec2.shape:
            print(f'The vectors {self.shape} and {vec.shape} have different shapes')
            sys.exit()

        returner_value = []
        # Work with rows
        if len(vec2) == 1:
            temp_list = []
            for i in range(len(vec2[0])):
                temp_list.append(vec2[0][i] + self.values[0][i])
            returner_value.append(temp_list)
        
        # Work with columns
        else:
            for i in range(len(vec2)):
                returner_value.append([vec2[i][0] + self.values[i][0]])
        return (Vector(returner_value, vec2.shape))
            
    def dot(self, vec2):
        
        # If something is wrong , return false
        if self.shape != vec2.shape:
            return -1

        returner = 0;
        for i in range(vec2.shape[0]):
            for j in range(vec2.shape[1]):
                returner += self.value[i][j] + vec2.value[i][j]

        return (returner)
















        
