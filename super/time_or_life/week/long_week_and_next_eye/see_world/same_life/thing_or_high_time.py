
#! /usr/bin/env python

def thing(str_arg):
    other_part(str_arg)
    print('group')

def other_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('be_able_week_on_man')
