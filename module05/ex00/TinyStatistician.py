# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    TinyStatistician.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/13 15:51:17 by akalimol          #+#    #+#              #
#    Updated: 2022/12/13 16:48:44 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import math

class TinyStatistician:
    
    def mean(self, x):

        x_len = len(x)
        x_sum = 0
        if x_len == 0:
            return None

        for elem in x:
            x_sum += elem
        return float(x_sum / x_len)

    def median(self, x):
        x_len = len(x)

        if x_len == 0:
            return None
        x.sort()
        if x_len % 2 == 1:
            return float(x[int(x_len / 2)])
        else:
            return float((x[x_len / 2] + x[x_len / 2 - 1]) / 2)

    def quartile(self, x):
        x_len = len(x)

        if x_len == 0:
            return None
        x.sort()
        if x_len % 4 == 0:
            return (x[x_len / 4] + x[x_len / 4 - 1]) / 2
        else:
            return [float(x[int(x_len / 4)]), float(x[int(x_len - x_len / 4)])]
    
    def var(self, x):
        x_len = len(x)
        if x_len == 0:
            return 0

        x_mean = self.mean(x)
        x_numerator = 0
        for num in x:
            x_numerator += abs(num - x_mean)**2
        return x_numerator / x_len

    def percentile(self, x, percent):
        x.sort()
        if (percent == 100):
            return (x[len(x) - 1])
        n_big = percent / 100 * (len(x) - 1) + 1
        n = math.floor(n_big)
        return x[n - 1] + (n_big - n) * (x[n] -x[n - 1])

    def std(self, x):
        returner = math.sqrt(self.var(x))
        if returner is None:
            return None
        return returner
