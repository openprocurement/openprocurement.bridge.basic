# -*- coding: utf-8 -*-
import os

from yaml import safe_load


DB_HOST = os.environ.get('DB_HOST', '')
DB_PORT = os.environ.get('DB_PORT', '')
DB_USER = os.environ.get('DB_USER', '')
DB_PASS = os.environ.get('DB_PASS', '')
CONFIG_FILE = "{}/test.yml".format(os.path.dirname(__file__))
with open(CONFIG_FILE, 'r') as f:
    TEST_CONFIG = safe_load(f.read())
if DB_HOST:
    TEST_CONFIG['main']['storage_config']['host'] = DB_HOST
if DB_PORT:
    TEST_CONFIG['main']['storage_config']['port'] = DB_PORT
if DB_USER:
    TEST_CONFIG['main']['storage_config']['user'] = DB_USER
if DB_PASS:
    TEST_CONFIG['main']['storage_config']['password'] = DB_PASS


class MockedResponse(object):

    def __init__(self, status_code, text=None, headers=None):
        self.status_code = status_code
        self.text = text
        self.headers = headers


class AlmostAlwaysTrue(object):

    def __init__(self, total_iterations=1):
        self.total_iterations = total_iterations
        self.current_iteration = 0

    def __nonzero__(self):
        if self.current_iteration < self.total_iterations:
            self.current_iteration += 1
            return bool(1)
        return bool(0)


class AdaptiveCache(object):

    def __init__(self, data):
        self.data = data

    def get(self, key):
        return self.data.get(key, '')

    def put(self, key, value):
        self.data[key] = value

    def has(self, key):
        return key in self.data

    def __getitem__(self, item):
        return self.data[item]

    def __contains__(self, item):
        return item in self.data
