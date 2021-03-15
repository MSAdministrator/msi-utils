import os
import subprocess


class MSICore:

    DATA_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')

    def get_path(self, value):
        return os.path.abspath(os.path.expanduser(os.path.expandvars(value)))

    def call_subprocess(self, value_list):
        return subprocess.check_call([x for x in value_list])