
#! /usr/bin/env python

def child(str_arg):
    time(str_arg)
    print('new_day')

def time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('first_world_and_fact')
