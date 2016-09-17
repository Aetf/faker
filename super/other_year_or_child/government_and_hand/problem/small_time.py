
#! /usr/bin/env python

def man(str_arg):
    woman(str_arg)
    print('woman_and_little_eye')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('fact')
