
#! /usr/bin/env python

def important_place(str_arg):
    world(str_arg)
    print('other_time')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    important_place('person_or_thing')
