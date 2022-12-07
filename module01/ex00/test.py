# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/06 14:14:45 by akalimol          #+#    #+#              #
#    Updated: 2022/12/06 19:28:51 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from recipe import Recipe
from book import Book


myRecipe = Recipe("croissant", 10, ["sugar", "flour", "butter"], "Vualiya", "dessert")
print(str(myRecipe))

myBook = Book("I am going to pizza")
myBook.add_recipe(myRecipe)
myBook.get_recipe_by_name("croissant")
