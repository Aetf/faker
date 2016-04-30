
#! /usr/bin/env python

def same_work(str_arg):
    work(str_arg)
    print('eye')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_work('find_hand')
