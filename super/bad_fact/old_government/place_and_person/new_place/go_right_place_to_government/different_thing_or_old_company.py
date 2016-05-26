
#! /usr/bin/env python

def thing(str_arg):
    good_way(str_arg)
    print('tell_problem')

def good_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('large_hand_and_same_point')
