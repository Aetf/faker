
#! /usr/bin/env python

def thing(str_arg):
    work(str_arg)
    print('child')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('new_hand_or_next_work')
