
#! /usr/bin/env python

def good_case(str_arg):
    hand(str_arg)
    print('old_number')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_case('time_or_next_life')
