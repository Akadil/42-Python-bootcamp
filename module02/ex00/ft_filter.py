# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/07 14:09:01 by akalimol          #+#    #+#              #
#    Updated: 2022/12/07 14:09:19 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from collections.abc import Iterable

def ft_filter(function_to_apply, iterable):
    
    """
    Filter the result of function apply to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """

    if isinstance(iterable, Iterable) is False:
        raise TypeError(f'{str(iterable)} is not an iterable')
    try:
        for element in iterable:
            if function_to_apply(element) is True:
                yield element
    except:
        return None
