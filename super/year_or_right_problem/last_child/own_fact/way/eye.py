
#! /usr/bin/env python

def early_world(str_arg):
    government(str_arg)
    print('old_point')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_world('life')
