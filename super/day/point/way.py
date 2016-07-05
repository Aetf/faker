
#! /usr/bin/env python

def long_work_or_different_time(str_arg):
    important_fact(str_arg)
    print('early_way')

def important_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_work_or_different_time('call_old_woman')
