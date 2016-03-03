
#! /usr/bin/env python

def child(str_arg):
    time_or_child(str_arg)
    print('give_work')

def time_or_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('way')
