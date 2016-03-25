
#! /usr/bin/env python

def time(str_arg):
    few_work(str_arg)
    print('time')

def few_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time('child')
