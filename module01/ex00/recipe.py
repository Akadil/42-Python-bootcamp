# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/06 12:45:48 by akalimol          #+#    #+#              #
#    Updated: 2022/12/06 14:49:44 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class   Recipe:
    name: str
    cooking_lvl = 2
    cooking_time: int
    ingredients: list
    descriptions: str
    recipe_type: str

    def __init__(self, name, cooking_time, ingredients, descriptions, recipe_type):
        self.name = name
        
        ##if cooking_lvl not in [1, 2, 3, 4, 5]:
        ##    print("The cooking level should be between 1 to 5")
        ##    sys.exit()
        ##self.cooking_lvl = cooking_lvl
        
        if cooking_time < 0:
            print("Cooking time couldn't be negative")
            sys.exit()
        self.cooking_time = cooking_time
        
        for ingredient in ingredients:
            if type(ingredient) is not str:
                print("One of your ingredients is not string")
                sys.exit()
        self.ingredients = ingredients
        
        self.descriptions = descriptions
        
        if recipe_type not in ["starter", "lunch", "dessert"]:
            print("The recipe type should be one of ", str(["starter", "lunch", "dessert"]))
            sys.exit()
        self.recipe_type = recipe_type

    def __str__(self):
        txt = ""
        txt = txt + "Name: " + self.name + "Cooking level: " + str(self.cooking_lvl)
        txt = txt + "Cooking time: " + str(self.cooking_time) + "Ingredients: " + str(self.ingredients)
        txt = txt + "Description: " + self.descriptions + "Recipe type: " + self.recipe_type
        return txt

