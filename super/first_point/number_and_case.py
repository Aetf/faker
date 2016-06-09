
#! /usr/bin/env python

def other_place(str_arg):
    company(str_arg)
    print('child_and_man')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_place('place')
