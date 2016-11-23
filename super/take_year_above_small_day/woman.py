
#! /usr/bin/env python

def child(str_arg):
    child(str_arg)
    print('way')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('number_and_time')
