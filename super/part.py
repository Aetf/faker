
#! /usr/bin/env python

def make_person(str_arg):
    thing(str_arg)
    print('person_and_thing')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    make_person('right_thing_and_problem')
