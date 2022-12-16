# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/14 17:44:49 by akalimol          #+#    #+#              #
#    Updated: 2022/12/14 18:04:37 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ImageProcessor import ImageProcessor

imp = ImageProcessor()
arr = imp.load("./dog.png")
"""
imp = ImageProcessor()
arr = imp.load("non_existing_file.png")
# Output :
# Exception: FileNotFoundError -- strerror: No such file or directory

print(arr)
# Output :
# None


arr = imp.load("empty_file.png")
# Output :
# Exception: OSError -- strerror: None

print(arr)
# Output :
# None


arr = imp.load("../resources/42AI.png")
# Output :
# Loading image of dimensions 200 x 200

print(arr)
# Big matrix
"""
