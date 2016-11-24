
#! /usr/bin/env python

def day_or_next_child(str_arg):
    own_child(str_arg)
    print('different_problem')

def own_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    day_or_next_child('eye_or_good_life')
