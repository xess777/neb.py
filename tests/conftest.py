import sys

pytest_plugins = ['account_fixtures']


def pytest_ignore_collect(path, config):
    if sys.version_info < (3, 6, 0):
        return True
