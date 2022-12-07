# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/06 13:28:33 by akalimol          #+#    #+#              #
#    Updated: 2022/12/06 15:53:38 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from recipe import Recipe

class Book:
    name: str
    last_update: time
    creation_date: time
    recipes_list: dict

    def __init__(self, name):
        self.name = name
        self.last_update = time.time()
        self.creation_date = time.time()
        self.recipes_list = {"starter":[], "lunch":[], "dessert":[]}

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipe_list in self.recipes_list.values():
            for recipe in recipe_list:
                if recipe.name is name:
                    print(str(recipe))
                    return (recipe)
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        returner = []
        for recipe_list in self.recipes_list.values():
            for recipe in recipe_list:
                if recipe.recipe_type is recipe_type:
                    returner.append(recipe.name)
        return returner

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe) is False:
            print("Error! wrong instance")
            sys.exit()
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = time.time()
