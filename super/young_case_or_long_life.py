
#! /usr/bin/env python

def life(str_arg):
    old_work(str_arg)
    print('child')

def old_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life('public_child_and_little_person')
