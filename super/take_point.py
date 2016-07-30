
#! /usr/bin/env python

def problem(str_arg):
    own_man_and_thing(str_arg)
    print('public_man')

def own_man_and_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    problem('time_and_good_week')
