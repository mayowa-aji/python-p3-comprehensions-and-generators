#!/usr/bin/env python3
# spot = [returned pet/loop/conditional]



def return_evens(num_list):
    num_list = [num for num in num_list if num % 2 == 0]
    return(num_list)


def make_exclamation(sentence_list):
    new_list = [list + '!' for list in sentence_list]
    return(new_list)
