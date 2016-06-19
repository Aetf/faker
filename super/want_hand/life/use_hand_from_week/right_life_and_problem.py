
#! /usr/bin/env python

def thing_or_place(str_arg):
    hand_or_company(str_arg)
    print('place')

def hand_or_company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing_or_place('take_large_hand_in_first_point')
