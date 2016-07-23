
#! /usr/bin/env python

def different_way(str_arg):
    old_work_or_group(str_arg)
    print('work')

def old_work_or_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_way('way')
