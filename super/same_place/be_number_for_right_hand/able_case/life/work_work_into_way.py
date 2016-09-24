
#! /usr/bin/env python

def own_way(str_arg):
    own_week(str_arg)
    print('week')

def own_week(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_way('thing')
