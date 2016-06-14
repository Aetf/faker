
#! /usr/bin/env python

def man(str_arg):
    world(str_arg)
    print('man')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('say_little_case_over_large_child')
