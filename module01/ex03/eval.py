# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalimol <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/06 17:15:14 by akalimol          #+#    #+#              #
#    Updated: 2022/12/06 17:18:09 by akalimol         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class   Evaluator:
    def zip_evaluate(coefs, words):
        sum = 0
        for i in range(len(coefs)):
            sum += coefs[i] * len(words[i])
        return sum

    def enumerate_evaluate(coefs, words):
        sum = 0
        for i in range(len(coefs)):
            sum += coefs[i] * len(words[i])
        return sum
