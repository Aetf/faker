
#! /usr/bin/env python

def see_person_with_day(str_arg):
    try_person_of_next_child(str_arg)
    print('right_number')

def try_person_of_next_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_person_with_day('place')
