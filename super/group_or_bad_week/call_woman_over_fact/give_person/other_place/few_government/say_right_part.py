
#! /usr/bin/env python

def hand_and_way(str_arg):
    hand_and_thing(str_arg)
    print('way')

def hand_and_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand_and_way('work')
