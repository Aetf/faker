
#! /usr/bin/env python

def see_life(str_arg):
    place_or_other_person(str_arg)
    print('person')

def place_or_other_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_life('case')
