
#! /usr/bin/env python

def company(str_arg):
    life(str_arg)
    print('child')

def life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company('be_able_thing')
