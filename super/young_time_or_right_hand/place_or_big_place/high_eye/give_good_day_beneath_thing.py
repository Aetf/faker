
#! /usr/bin/env python

def fact(str_arg):
    call_next_way(str_arg)
    print('group')

def call_next_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    fact('man_or_good_hand')
