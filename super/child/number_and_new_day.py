
#! /usr/bin/env python

def group(str_arg):
    important_hand(str_arg)
    print('other_thing_and_child')

def important_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    group('person')
