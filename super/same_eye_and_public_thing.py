
#! /usr/bin/env python

def life(str_arg):
    person(str_arg)
    print('child')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life('early_eye')
