# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/18 11:40:26 by akalimol          #+#    #+#              #
#    Updated: 2022/12/18 12:31:25 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if __name__ == "__main__":
    
    # Take the characters from terminal
    list_of_inputs = sys.argv[1:]

    # Check for existence of inputs
    if len(list_of_inputs) == 0:
        print("The string to convert wasn't given:(")
        sys.exit()
    
    # Check for correctness of the inputs
    for elem in list_of_inputs:
        if elem.replace(' ', '').isalnum() == 0:
            print(f'The string "{elem}" is wrong formatted')
            sys.exit()

    # Morse code dictionary
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----'}

    #  
    for i in range(0, len(list_of_inputs)):

        # Print / if not first string
        if i != 0:
            print("/", end = '')

        # Change string to upper for compatibility with dict
        elem = list_of_inputs[i].upper()
        for char in elem:
            if char.isspace() == 1:
                print('/', end = '');
                continue
            print(MORSE_CODE_DICT[char], end = '')
