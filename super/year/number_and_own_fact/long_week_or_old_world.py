
#! /usr/bin/env python

def child(str_arg):
    child(str_arg)
    print('week_or_important_work')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('come_world')
