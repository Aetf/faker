
#! /usr/bin/env python

def work(str_arg):
    place(str_arg)
    print('world')

def place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('small_man')
