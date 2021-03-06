#!/usr/bin/python

import sys
sys.path += (sys.path[0] + '/..')

import re
import record
rs = record.AllRecords()

for r in rs:
  if r.location():
    # remove leading 'Folder: ', trailing period & convert various forms of
    # dashes to a single form of slashes.
    folder = r.location()
    if folder:
      if folder[-1] == '.' and not folder[-3] == '.':  # e.g. 'Y.M.C.A'
        folder = folder[:-1]
      folder = folder.replace('Folder: ', '')
      folder = re.sub(r' *- *', ' / ', folder)
    print folder
  else:
    print '(none)'
