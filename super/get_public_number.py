
#! /usr/bin/env python

def young_thing(str_arg):
    different_part(str_arg)
    print('other_thing')

def different_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    young_thing('want_old_person_about_bad_fact')
