
#! /usr/bin/env python

def person(str_arg):
    do_person_into_life(str_arg)
    print('right_place')

def do_person_into_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('different_group')
