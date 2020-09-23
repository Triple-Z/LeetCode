#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import argparse
import logging

from datetime import datetime
from pathlib import Path
from urllib.parse import quote
from problem import Problem
from jinja2 import FileSystemLoader, Environment


def main():
    logging.basicConfig(level=logging.DEBUG)
    # get root directory
    cwd = Path(__file__).parents[0]
    root_dir = cwd / '..'
    # set argprase
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-i', '--interactive', dest='is_interactive', action='store_true', default=False)

    args = parser.parse_args()
    is_interactive = args.is_interactive

    # TODO: interactive input problem info(number, title_en, title_zh, difficulty, topics, link)
    if is_interactive:
        logging.debug("TODO")
    # TODO: input via command line

if __name__ == "__main__":
    main()