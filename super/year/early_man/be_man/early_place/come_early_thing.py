
#! /usr/bin/env python

def say_eye(str_arg):
    woman(str_arg)
    print('world')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_eye('work')