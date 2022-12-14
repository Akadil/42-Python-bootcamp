# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tools.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/13 18:43:06 by akalimol          #+#    #+#              #
#    Updated: 2022/12/14 17:02:01 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def add_intercept(x):
    
    """Adds a column of 1’s to the non-empty numpy.array x.
    Args:
        x: has to be a numpy.array of dimension m * n.
    Returns:
        X, a numpy.array of dimension m * (n + 1).
        None if x is not a numpy.array.
        None if x is an empty numpy.array.
    Raises:
        This function should not raise any Exception.
    """
    
    len_x = x.shape[0]
    list1 = [1 for i in range(len(x))]
    np.concatenate([list1, x], axis=1)
    x_1 = np.array([1 for i in range(x.shape[0])])
    np.concantenate
