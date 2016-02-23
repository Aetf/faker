
#! /usr/bin/env python

def little_eye(str_arg):
    thing(str_arg)
    print('child')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_eye('government_and_big_part')
