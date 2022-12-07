# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 16:06:56 by akalimol          #+#    #+#              #
#    Updated: 2022/12/05 16:41:52 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

my_argv = sys.argv[1:]

for i in range(len(my_argv)):
    print(my_argv[i][::-1].swapcase(), end='')
    if i != len(my_argv) - 1:
        print(' ', end='')
