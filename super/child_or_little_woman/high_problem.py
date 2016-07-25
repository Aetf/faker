
#! /usr/bin/env python

def man(str_arg):
    tell_last_case(str_arg)
    print('able_work')

def tell_last_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('child')
