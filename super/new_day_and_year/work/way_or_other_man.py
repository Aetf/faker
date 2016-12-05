
#! /usr/bin/env python

def man(str_arg):
    say_child(str_arg)
    print('right_hand')

def say_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('woman')
