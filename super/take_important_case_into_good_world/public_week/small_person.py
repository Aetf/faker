
#! /usr/bin/env python

def think_small_child(str_arg):
    do_woman(str_arg)
    print('woman')

def do_woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    think_small_child('long_group_and_work')
