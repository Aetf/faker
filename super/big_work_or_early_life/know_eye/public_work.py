
#! /usr/bin/env python

def use_different_hand_for_own_fact(str_arg):
    big_thing(str_arg)
    print('woman')

def big_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_different_hand_for_own_fact('time')
