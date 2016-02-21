
#! /usr/bin/env python

def child(str_arg):
    tell_other_work(str_arg)
    print('last_part')

def tell_other_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('use_government_of_woman')
