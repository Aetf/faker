
#! /usr/bin/env python

def use_good_way_above_person(str_arg):
    fact(str_arg)
    print('person')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_good_way_above_person('old_man')
