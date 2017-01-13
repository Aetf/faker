#! /usr/bin/env python

from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from commitfaker import commitonday
from sys_util import git_tag


class Cell:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)


class DatedBitmap(object):
    def __init__(self, columns=None):
        super(DatedBitmap, self).__init__()
        self.start_date = None
        self.nrow = 7
        self.ncol = 0
        self.size = 0
        self.cells = []
        if columns is not None:
            self._parse(columns)

    def _parse(self, columns):
        self.ncol = len(columns)
        for col in columns:
            for elm in col.select('rect'):
                self.cells.append(int(elm['data-count']))
                d = datetime.strptime(elm['data-date'], '%Y-%m-%d').date()
                if self.start_date is None:
                    self.start_date = d
        self.size = len(self.cells)

    def _tolinear(self, xidx, yidx):
        return xidx * self.nrow + yidx

    def _valid(self, xidx, yidx):
        return self._tolinear(xidx, yidx) < len(self.cells)

    def _at(self, xidx, yidx):
        return self.cells[self._tolinear(xidx, yidx)]

    def at(self, idx, yidx=None):
        if yidx is not None:
            idx = self._tolinear(idx, yidx)

        obj = Cell()
        obj.count = self.cells[idx]
        obj.date = self.start_date + timedelta(days=idx)
        return obj

    def diffwitheven(self):
        replica = DatedBitmap()
        replica.start_date = self.start_date
        replica.nrow = self.nrow
        replica.ncol = self.ncol
        replica.size = self.size
        base = max(self.cells)
        replica.cells = [base - v for v in self.cells]
        return replica

    def bmpstr(self):
        bmp = ''
        for yidx in range(self.nrow):
            for xidx in range(self.ncol):
                if self._valid(xidx, yidx):
                    bmp += '{: <2}'.format(self._at(xidx, yidx))
            bmp += '\n'
        return bmp

    def __repr__(self):
        return 'DatedBitmap(ncol={}, nrow={}, start_date={})\n{}'.format(self.ncol, self.nrow,
                                                                         self.start_date,
                                                                         self.bmpstr())


def getUserBMP(username):
    endpoint = 'https://github.com/Aetf'
    r = requests.get(endpoint)
    soup = BeautifulSoup(r.text, 'html.parser')
    gs = soup.select('svg.js-calendar-graph-svg g:nth-of-type(1) g')

    bmp = DatedBitmap(gs)
    return bmp


if __name__ == '__main__':
    bmp = getUserBMP('Aetf')

    print('Got your activity map:')
    print(bmp.bmpstr())

    restore = 'restore_point{:%Y%m%d%H%M%s}'.format(datetime.now())
    git_tag(restore)
    diff = bmp.diffwitheven()

    print('This will be the diff to make it even')
    print(diff.bmpstr())

    for idx in tqdm(range(diff.size)):
        cell = diff.at(idx)
        if cell.count > 0:
            tqdm.write('Generating {} commits on {}'.format(cell.count, cell.date))
            commitonday(cell.date, cell.count)

    print('\nDone. Now you can do a git push, or restore to tag', restore)
