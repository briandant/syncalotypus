#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `syncalotypus` package."""

import pytest

from click.testing import CliRunner

from syncalotypus import syncalotypus
from syncalotypus import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'syncalotypus.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_load_yaml():
    """I can load a yml file."""
    syncalotypus.load_config()


def test_parse_entry():
    """An entry with the proper attributes can be parsed."""
    pytest.fail()


def test_raise_missing_attr():
    """If an entry does not have the proper fields, we raise."""
    pytest.fail()
