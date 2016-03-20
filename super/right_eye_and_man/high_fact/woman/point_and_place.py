
#! /usr/bin/env python

def man(str_arg):
    child(str_arg)
    print('same_day')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('think_person')
