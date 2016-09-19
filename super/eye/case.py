
#! /usr/bin/env python

def big_work(str_arg):
    little_woman(str_arg)
    print('own_hand')

def little_woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_work('say_number')
