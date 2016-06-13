
#! /usr/bin/env python

def take_hand_to_work(str_arg):
    place(str_arg)
    print('work')

def place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    take_hand_to_work('number')
