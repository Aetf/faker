
#! /usr/bin/env python

def eye(str_arg):
    look_place_with_first_time(str_arg)
    print('call_long_time')

def look_place_with_first_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye('own_number_and_long_case')
