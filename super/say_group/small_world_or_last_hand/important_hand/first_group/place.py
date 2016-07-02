
#! /usr/bin/env python

def case(str_arg):
    number(str_arg)
    print('child_and_other_child')

def number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case('good_hand')
