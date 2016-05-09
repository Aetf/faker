
#! /usr/bin/env python

def time(str_arg):
    day(str_arg)
    print('child')

def day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time('little_person')
