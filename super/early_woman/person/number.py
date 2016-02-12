
#! /usr/bin/env python

def want_man(str_arg):
    hand(str_arg)
    print('hand')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    want_man('problem_and_person')
