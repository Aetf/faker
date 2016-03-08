
#! /usr/bin/env python

def place_and_eye(str_arg):
    man(str_arg)
    print('man')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    place_and_eye('way')
