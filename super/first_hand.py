
#! /usr/bin/env python

def person(str_arg):
    bad_person(str_arg)
    print('first_world')

def bad_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('go_great_life')
