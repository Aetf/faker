
#! /usr/bin/env python

def thing_and_person(str_arg):
    same_thing(str_arg)
    print('big_group')

def same_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing_and_person('fact')
