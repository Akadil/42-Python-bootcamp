# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    FileLoader.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/09 14:22:22 by akalimol          #+#    #+#              #
#    Updated: 2022/12/09 16:01:18 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import os

class FileLoader:
    
    """
    A class containing a load and a display method
    """

    @staticmethod
    def load(path):
        """ load(self, path): takes as an argument the file path of the dataset to load,
            displays a message specifying the dimensions of the dataset (e.g. 340 x 500) and
            returns the dataset loaded as a pandas.DataFrame.
        """
        if os.path.isfile(path) is False:
            print("No such file")
            return None
        try:
            
            if path[-4:] == ".csv":
                df = pd.read_csv(path, index_col=0)
            else:
                data = open(path, "r")
                df = pd.DataFrame(df)
            print(df.shape)
        except:
            print("Couldn't read the file")
            df = None
        return df

    @staticmethod
    def display(df, n):
        """
        display(self, df, n): takes a pandas.DataFrame and an integer as arguments,
displays the first n rows of the dataset if n is positive, or the last n rows if n is
negative.
        """
        if isinstance(df, pd.DataFrame) is False:
            print(f'given dataframe is not a dataframe!')
            return
        if n >= 0:
            print(df[:n])
        else:
            print(df[n:])


