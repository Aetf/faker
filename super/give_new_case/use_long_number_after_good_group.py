
#! /usr/bin/env python

def day(str_arg):
    new_child(str_arg)
    print('call_other_problem')

def new_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    day('say_able_year_about_way')
