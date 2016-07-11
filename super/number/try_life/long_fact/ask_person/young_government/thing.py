
#! /usr/bin/env python

def other_thing(str_arg):
    able_part(str_arg)
    print('child_and_able_person')

def able_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_thing('leave_life_under_different_point')
