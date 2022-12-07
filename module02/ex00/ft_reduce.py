# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/07 14:08:28 by akalimol          #+#    #+#              #
#    Updated: 2022/12/07 14:09:35 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from collections.abc import Iterable

def ft_reduce(function_to_apply, iterable):
    
    """
    Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """
    
    if isinstance(iterable, Iterable) is False:
        raise TypeError(f'{str(iterable)} is not an iterable') 
    try:
        for ind, element in enumerate(iterable):
            if ind == 0:
                returner = elemet
            else:
                returner = function_to_apply(returner, element)
        return returner
    except:
        return None

