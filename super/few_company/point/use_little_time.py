
#! /usr/bin/env python

def see_person(str_arg):
    call_hand_for_young_man(str_arg)
    print('world')

def call_hand_for_young_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_person('big_way')
