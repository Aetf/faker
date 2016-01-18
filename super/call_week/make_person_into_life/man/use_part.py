
#! /usr/bin/env python

def child_and_problem(str_arg):
    early_hand(str_arg)
    print('first_fact')

def early_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_problem('ask_next_way')
