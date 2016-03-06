
#! /usr/bin/env python

def important_child(str_arg):
    next_case(str_arg)
    print('say_right_way')

def next_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    important_child('number')
