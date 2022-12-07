# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/06 15:55:13 by akalimol          #+#    #+#              #
#    Updated: 2022/12/06 16:24:03 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
    first_name: str
    is_alive = True

    def __init__(self, name, is_alive):
        self.first_name = name
        self.is_alive = is_alive

class Stark(GotCharacter):
    """
    My first docstring
    """
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
