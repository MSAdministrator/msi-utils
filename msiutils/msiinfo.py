from .msicore import MSICore
from .msidiff import MSIDiff


class MSIInfo(MSICore):

    def streams(self, path):
        return self.call_subprocess(['{}/msiinfo'.format(self.DATA_PATH), 'streams', path])

    def tables(self, path):
        return self.call_subprocess(['{}/msiinfo'.format(self.DATA_PATH), 'tables', path])

    def summary(self, path):
        return self.call_subprocess(['{}/msiinfo'.format(self.DATA_PATH), 'suminfo', path])

    def diff(self):
        return MSIDiff()
