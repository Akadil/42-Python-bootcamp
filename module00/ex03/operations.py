# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 18:42:50 by akalimol          #+#    #+#              #
#    Updated: 2022/12/05 19:04:05 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

my_list = sys.argv[1:]
if len(my_list) == 0:
    print("Usage advice")
elif len(my_list) != 2:
    print("Too many arguments")
else:
    try:
        num1 = int(my_list[0])
        num2 = int(my_list[1])

        print(f'Sum:        {num1 + num2}')
        print(f'Difference: {num1 - num2}')
        print(f'Product:    {num1 * num2}')
        if num2 == 0:
            print("error")
            print("Error")
        else:
            print(f'Quotient:     {num1 / num2}')
            print(f'Remainder:    {num1 % num2}')
    except:
        print("Integers only")

