import numpy as np

class NumpyCreator:

    def from_list(self, lst):

        # Check if lst is list
        if type(lst) is not list:
            return None

        # The basic case
        if len(lst) == 1:
            return np.array(lst)
        
        # Check for inconvenient shapes
        same_length = len(lst[0])
        for i in range(1, len(lst)):
            if len(lst[i]) != same_length:
                return None
        
        # Check for the types of the matrix inputs
        type_of_input = type(lst[0][0])
        for i in range(0, len(lst)):
            for inp in lst[0]:
                if type(inp) != type_of_input:
                    return np.array(lst, dtype='s')

        return np.array(lst)


    def from_tuple(self, tpl):

        # Check for the type
        if type(tpl) is not tuple:
            return None

        return np.array(tpl)


    def from_iterable(self, itr):
        return np.array(itr)

    def from_shape(self, shape, value):
        return np.full(shape, value)

    def random(self, shape):
        print("Hello world")

    def identity(self, n):
        return np.identity(n)

"""
https://www.w3schools.com/python/numpy/numpy_data_types.asp 
The source for exploring the types of inputs

"""
