
#! /usr/bin/env python

def bad_eye(str_arg):
    way(str_arg)
    print('call_work')

def way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_eye('different_government')
