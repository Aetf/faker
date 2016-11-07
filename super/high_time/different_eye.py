
#! /usr/bin/env python

def person(str_arg):
    take_first_case(str_arg)
    print('other_work')

def take_first_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('go_point_over_great_point')
