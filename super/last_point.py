
#! /usr/bin/env python

def early_child(str_arg):
    next_hand(str_arg)
    print('hand')

def next_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_child('same_government')
