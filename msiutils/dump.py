from .msicore import MSICore


class MSIDump(MSICore):

    def tables(self, path, output='./'):
        return self.call_subprocess(['{}/msidump'.format(self.DATA_PATH), '--tables', '--directory', self.get_path(output), path])

    def streams(self, path, output='./'):
        return self.call_subprocess(['{}/msidump'.format(self.DATA_PATH), '--streams', '--directory', self.get_path(output), path])

    def signature(self, path, output='./'):
        return self.call_subprocess(['{}/msidump'.format(self.DATA_PATH), '--signature', '--directory {}', self.get_path(output), path])
