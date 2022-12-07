# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/06 16:24:24 by akalimol          #+#    #+#              #
#    Updated: 2022/12/06 17:11:43 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import sys

def generator(text, seps=" ", options=None):
    if text.isprintable() is False or type(text) is not str:
        print("unprintable character", letter)
        sys.exit()

    container = text.split()
    my_len = len(container)

    if options == "shuffle":
        for i in range(my_len):
            my_index = random.randint(1, my_len - i) - 1
            yield container[my_index]
            container.pop(my_index)
    
    elif options == "unique":
        already_used = []
        for obj in container:
            if obj not in already_used:
                already_used.append(obj)
                yield obj

    elif options == "ordered":
        container.sort()
        for obj in container:
            yield obj
    
    else:
        for obj in container:
            yield obj
