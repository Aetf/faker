
#! /usr/bin/env python

def bad_child(str_arg):
    way(str_arg)
    print('ask_time')

def way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_child('group')
