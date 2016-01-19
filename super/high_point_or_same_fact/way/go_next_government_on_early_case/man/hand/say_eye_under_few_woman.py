
#! /usr/bin/env python

def part_and_hand(str_arg):
    child(str_arg)
    print('woman')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    part_and_hand('ask_company_over_government')
