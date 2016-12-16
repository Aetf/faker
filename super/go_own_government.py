
#! /usr/bin/env python

def child_or_great_part(str_arg):
    look_able_fact(str_arg)
    print('come_work_to_child')

def look_able_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_or_great_part('long_day')
