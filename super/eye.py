
#! /usr/bin/env python

def use_place(str_arg):
    make_woman(str_arg)
    print('other_case')

def make_woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_place('ask_fact_above_able_point')
