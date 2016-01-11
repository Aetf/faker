
#! /usr/bin/env python

def use_case_after_important_thing(str_arg):
    man_and_long_number(str_arg)
    print('case')

def man_and_long_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_case_after_important_thing('same_part')
