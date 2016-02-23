
#! /usr/bin/env python

def take_thing_into_time(str_arg):
    work_world(str_arg)
    print('small_work')

def work_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    take_thing_into_time('life')
