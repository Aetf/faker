
#! /usr/bin/env python

def think_part_after_work(str_arg):
    week_or_day(str_arg)
    print('important_week')

def week_or_day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    think_part_after_work('work')
