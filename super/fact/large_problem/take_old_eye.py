
#! /usr/bin/env python

def big_world(str_arg):
    own_work(str_arg)
    print('tell_world')

def own_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_world('long_person')
