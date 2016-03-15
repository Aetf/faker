
#! /usr/bin/env python

def large_work(str_arg):
    life(str_arg)
    print('long_hand')

def life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_work('important_place_and_time')
