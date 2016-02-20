
#! /usr/bin/env python

def child(str_arg):
    fact(str_arg)
    print('work_group')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('world_and_part')
