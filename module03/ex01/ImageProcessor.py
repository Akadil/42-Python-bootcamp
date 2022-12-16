# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/14 17:44:49 by akalimol          #+#    #+#              #
#    Updated: 2022/12/14 18:10:07 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as pyplot
import matplotlib.image as mpimg


class ImageProcessor:
    
    @staticmethod
    def load(path):
        im = pyplot.imread(path)
        
        pyplot.figure(figsize = (im.shape[1] / pyplot.rcParams['savefig.dpi'], im.shape[0] / pyplot.rcParams['savefig.dpi']))
        pyplot.axis('off')
        pyplot.gcf().subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
        pyplot.imshow(im)
        pyplot. savefig('myImage.png')

        pyplot.axis('off')
        pyplot.xlim(0, 1) # to indicate dimensions
        pyplot.ylim(0, 1) # to indicate dimensions
        pyplot. imshow(im, extent = [0, 0.2, 0.6, 0.8]) # xmin, xmax, ymin, ymax

    @staticmethod
    def display(array):
        print("Hello world!")
