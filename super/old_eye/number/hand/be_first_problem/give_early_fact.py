
#! /usr/bin/env python

def thing_and_person(str_arg):
    work(str_arg)
    print('same_hand')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing_and_person('hand')
