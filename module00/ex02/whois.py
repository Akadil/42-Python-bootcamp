# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 16:43:28 by akalimol          #+#    #+#              #
#    Updated: 2022/12/05 16:58:14 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

myList = sys.argv[1:]
if len(myList) != 0:
    if len(myList) > 1:
        print("AssertionError: more than one argument are provided")
    else:
        try:
            myNum = int(myList[0])
            if myNum == 0:
                print("I'm Zero.")
            elif myNum % 2 == 0:
                print("I am Even.")
            else:
                print("I am Odd.")
        except:
            print("AssertionError: argument is not an integer")

    
