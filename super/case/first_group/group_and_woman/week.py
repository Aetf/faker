
#! /usr/bin/env python

def other_child(str_arg):
    get_thing(str_arg)
    print('world')

def get_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_child('call_way')
