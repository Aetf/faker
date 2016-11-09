
#! /usr/bin/env python

def use_child(str_arg):
    early_person(str_arg)
    print('new_week')

def early_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_child('year_or_next_company')
