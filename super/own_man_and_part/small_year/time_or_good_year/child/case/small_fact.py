
#! /usr/bin/env python

def eye(str_arg):
    own_child(str_arg)
    print('hand')

def own_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye('week')
