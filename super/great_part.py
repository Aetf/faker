
#! /usr/bin/env python

def few_child(str_arg):
    work(str_arg)
    print('last_world')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    few_child('man')
