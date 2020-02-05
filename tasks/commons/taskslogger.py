import argparse
import logging
import os
import sys
from configparser import ConfigParser
from enum import Enum
from getpass import getpass
from inspect import currentframe

import appdirs

from tasks import config as cfg
from tasks.commons import tasksutils as tu

loggerdict = {}


class TLogLevel(str, Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

def get_linenumber():
    cf = currentframe()
    return cf.f_back.f_lineno

def tlog(tloglevel, tmodulelogname, tpackagename, lineno, message):

    if tpackagename not in loggerdict:

        # get the last package name to retrieve the config name
        loggerconfig = tpackagename.rsplit(".", 1)[1]

        # retrieve config file if it exists and prefill defaults
        # config file can be in multiple locations
        configfile = tu.getconfigs() or None

        if configfile is not None:
            cfg = ConfigParser()
            cfg.read(configfile)

            enablelogging = cfg.getboolean(loggerconfig, "logenabled")

            # create the directory for the log if it does not exists
            # to avoid getting FileNotFoundError
            logfilename = cfg.get(loggerconfig, "logfilename")
            loglevel = cfg.get(loggerconfig, "loglevel")

        if enablelogging:

            logger = logging.getLogger(tpackagename)
            logger.setLevel(eval("logging.{}".format(loglevel)))

            f_handler = logging.FileHandler(logfilename)
            f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            f_handler.setFormatter(f_format)

            logger.addHandler(f_handler)

        loggerdict[tpackagename] = enablelogging

    else:

        logger = logging.getLogger(tpackagename)

    # if logging is enabled
    if loggerdict[tpackagename]:

        logmessage = "Line {} : {} : {}".format(lineno, tmodulelogname, message)

        if TLogLevel.DEBUG == tloglevel:
            logger.debug(logmessage)

        if TLogLevel.INFO == tloglevel:
            logger.info(logmessage)

        if TLogLevel.WARNING == tloglevel:
            logger.warning(logmessage)

        if TLogLevel.ERROR == tloglevel:
            logger.error(logmessage)

        if TLogLevel.CRITICAL == tloglevel:
            logger.critical(logmessage)
