# Copyright (c) Aniskov N., Birillo A.

import os
from enum import Enum

# src folder
ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../')
TEST_RESOURCES_PATH = os.path.join(ROOT_DIR, 'test', 'resources')

DEFAULT_ENCODING = 'utf-8'
ISO_ENCODING = 'ISO-8859-1'

LOGGER_NAME = 'main_logger'
LOGGER_FORMAT = '%(asctime)s:%(levelname)s ==> %(message)s'
LOGGER_FILE = os.path.join(ROOT_DIR, 'main', 'logs.log')
LOGGER_TEST_FILE = os.path.join(ROOT_DIR, 'test', 'logs.log')


class FILE_SYSTEM_ITEM(Enum):
    PATH = 0
    SUBDIR = 1
    FILE = 2
