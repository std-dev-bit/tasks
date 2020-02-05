import argparse
import os
import sys
from enum import Enum

from inspect import currentframe

import appdirs

from tasks import config as cfg

logpkgname = str(__package__)
logmodulename = __name__

CONFIG_FILE_NAME = "tasks"
CONFIG_FILE = "{}.cfg".format(CONFIG_FILE_NAME)

#
# directory search order for config file
#
#   current home directory : ~/.tasks.cfg
#   current home config directory : ~/.config/tasks/tasks.cfg
#   global /usr/local/etc/ : /usr/local/etc/tasks.cfg
#   DEFAULTS TO - project folder : /tasks/tasks/config/tasks.cfg
#

CONFIG_LOCATIONS = [
    "~/.{}".format(CONFIG_FILE),
    appdirs.user_config_dir(CONFIG_FILE),
    "/usr/local/etc/{}".format(CONFIG_FILE),
]


def getconfigs():

    for cfgfile in CONFIG_LOCATIONS:

        if os.path.exists(cfgfile):

            return cfgfile

        else:

            try:
                from importlib import resources
            except ImportError:
                import importlib_resources as resources

            with resources.path("tasks.config", "tasks.cfg") as path:
                return path
