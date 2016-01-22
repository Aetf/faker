
#! /usr/bin/env python

def group_and_bad_child(str_arg):
    hand(str_arg)
    print('hand')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    group_and_bad_child('good_man')
