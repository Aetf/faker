
#! /usr/bin/env python

def right_group(str_arg):
    first_hand(str_arg)
    print('child')

def first_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    right_group('tell_public_place_under_able_woman')
