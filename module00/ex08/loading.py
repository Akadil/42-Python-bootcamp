# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/19 14:45:36 by akalimol          #+#    #+#              #
#    Updated: 2022/12/19 15:34:50 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time 

def ft_progress(lst):
    l = len(lst)
    for i in range(l):
        print(f'[{int((i + 1) / 1000 * 100)}%]')
        yield lst[i]


if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)
