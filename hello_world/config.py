"""
config.py

A custom config yaml may be provided in the following locations:


<VIRTUAL-ENVIRONMENT-ROOT>/.hello-world/config.yaml   # environment config
~/.hello-world/config.yaml                            # user config
/.hello-world/config.yaml                             # global config

First, the environment config location is checked for a config file. If not
found, then the user location is checked, and if no config file is found,
the global config location is checked. If no config file is found, the default
config.yaml included in this package will be used.

"""

import os
from os.path import dirname, join
import sys
import yaml

_env_configpath = join(sys.exec_prefix, ".hello-world", "config.yaml")
_home_configpath = join(os.path.expanduser('~'), ".hello-world", "config.yaml")
_global_configpath = "/.hello-world/config.yaml"
_default_configpath = join(dirname(dirname(os.path.realpath(__file__))), "config.yaml")


def get_configpath() -> str:
    for path in [_env_configpath, _home_configpath, _global_configpath]:
        if os.path.exists(path):
            return path
    return _default_configpath

def get_config() -> dict:
    with open(get_configpath(), 'rt') as f:
        return yaml.load(f, Loader=yaml.FullLoader)


class _Config:
    
    def __init__(self):
        """This method is defined to remind you that this is not a static class"""

    @property
    def color(self):
        if self.get_test_mode_enabled():
            return get_config()['test_mode']['color']
        return get_config()['color']

    @property
    def attrs(self):
        if self.get_test_mode_enabled():
            return get_config()['test_mode']['attrs']
        return get_config()['attrs']

    def get_test_mode_enabled(self):
        _env_var = os.environ.get('HW_TEST_MODE_ENABLED')
        if not _env_var:
            return False    
        if _env_var.upper() == "TRUE":
            return True
        return False

    def set_test_mode_enabled(self, val: bool):
        if isinstance(val, bool):
            os.environ['HW_TEST_MODE_ENABLED'] = str(val).upper()
        else:
            raise TypeError(f"Must provide a bool, not a {type(val)}")

CONFIG = _Config()