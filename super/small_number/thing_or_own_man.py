
#! /usr/bin/env python

def think_child(str_arg):
    child(str_arg)
    print('new_day')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    think_child('day_and_different_man')
