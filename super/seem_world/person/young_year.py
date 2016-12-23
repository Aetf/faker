
#! /usr/bin/env python

def time_and_child(str_arg):
    hand(str_arg)
    print('have_problem')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time_and_child('child')
