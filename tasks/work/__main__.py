#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Work

Description:
------------

"""

import os

import csv
import json

import time

# local imports
from tasks.commons import tasksutils as tu
from tasks.commons import taskslogger as tl

logpkgname = str(__package__)
logmodulename = __name__

def main():

    tl.tlog(
        tl.TLogLevel.DEBUG, 
        logmodulename,
        logpkgname,
        tl.get_linenumber(),
        "Sample to Check Logs",
    )

if __name__ == "__main__":
    main()
