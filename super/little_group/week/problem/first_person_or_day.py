
#! /usr/bin/env python

def group_or_person(str_arg):
    young_case(str_arg)
    print('man')

def young_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    group_or_person('long_hand_and_case')
