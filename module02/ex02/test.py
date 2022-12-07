# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/07 16:07:52 by akalimol          #+#    #+#              #
#    Updated: 2022/12/07 16:18:23 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from TinyStatistician import TinyStatistician

tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]

print(tstat.mean(a))
# Expected result: 82.4

print(tstat.median(a))
# Expected result: 42.0

print(tstat.quartile(a))
# Expected result: [10.0, 59.0]

print(tstat.var(a))
# Expected result: 12279.439999999999

print(tstat.std(a))
# Expected result: 110.81263465868862
