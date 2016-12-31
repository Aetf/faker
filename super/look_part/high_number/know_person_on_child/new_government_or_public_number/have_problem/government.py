
#! /usr/bin/env python

def few_day_or_right_work(str_arg):
    work(str_arg)
    print('child')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    few_day_or_right_work('hand_or_same_work')
