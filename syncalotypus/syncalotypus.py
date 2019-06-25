# -*- coding: utf-8 -*-

"""Main module."""

from yaml import load  # , dump
# from yaml import Loader, Dumper

import settings


def load_config(config_filepath=None):
    """Given a config filepath, load the file into a yaml object and return it."""

    config_filepath = config_filepath or settings.CONFIG_FILEPATH

    with open(config_filepath) as f:
        return load(f)
