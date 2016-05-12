
#! /usr/bin/env python

def child(str_arg):
    world(str_arg)
    print('have_few_child')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('work_or_important_man')
