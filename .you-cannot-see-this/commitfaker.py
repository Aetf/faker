#! /usr/bin/env python

import os
from datetime import datetime, date

from tqdm import tqdm

from githubplayer import randfl, randmsg, mkdir, write2file, gen_code
from sys_util import git_rm, git_add, git_commit
from datetime_picker import dt_pick, dt2str, str2dt


def commitonday(date, freq):
    dst = datetime(date.year, date.month, date.day, 10, 0, 0)
    ded = datetime(date.year, date.month, date.day, 14, 59, 59)

    for dtime in tqdm(dt_pick(dt2str(dst), dt2str(ded), freq)):
        fakecommit(str2dt(dtime))


def fakecommit(time=None):
    # remove old files
    git_rm(['super'])
    # generate random files
    files = randfl('super')
    for f in files:
        mkdir(os.path.dirname(f))
        write2file(gen_code(), f)
    msg = randmsg(files)
    git_add(files)
    git_commit(msg, time)


if __name__ == '__main__':
    commitonday(date(2017, 4, 1), 4)
