
#! /usr/bin/env python

def tell_hand_to_thing(str_arg):
    make_thing_above_woman(str_arg)
    print('go_woman')

def make_thing_above_woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    tell_hand_to_thing('thing_and_important_hand')
