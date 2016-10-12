
#! /usr/bin/env python

def few_child(str_arg):
    child(str_arg)
    print('place')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    few_child('world_or_few_hand')
