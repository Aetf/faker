
#! /usr/bin/env python

def work_thing(str_arg):
    world(str_arg)
    print('eye')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_thing('public_number_and_place')
