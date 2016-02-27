
#! /usr/bin/env python

def child(str_arg):
    great_world_and_day(str_arg)
    print('big_thing')

def great_world_and_day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('group')
