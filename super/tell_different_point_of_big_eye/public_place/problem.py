
#! /usr/bin/env python

def man(str_arg):
    woman(str_arg)
    print('work')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('look_fact')
