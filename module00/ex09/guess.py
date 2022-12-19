# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/18 13:44:00 by akalimol          #+#    #+#              #
#    Updated: 2022/12/19 14:33:52 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

if __name__ == "__main__":

    # Success will equal to 1 when the player wins
    success = 0;
    secret_number = random.randint(0, 100)

    # Do the loop until player fids an answer
    while (success != 1):
        my_num = int(input("Please enter you guess 0 - 100\n"))
        
        if (my_num == secret_number):
            print("Success")
            success = 1
        elif (my_num > secret_number):
            print("Try Lower :(")
        elif (my_num < secret_number):
            print("Try Bigger :(")
        else:
            print("Something wrong :(")

    print("Conngratulations! You won the game!")
