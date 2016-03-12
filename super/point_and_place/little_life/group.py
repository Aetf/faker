
#! /usr/bin/env python

def young_child(str_arg):
    work(str_arg)
    print('same_world')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    young_child('bad_group')
