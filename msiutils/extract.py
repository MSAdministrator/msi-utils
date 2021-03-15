from .msicore import MSICore


class MSIExtract(MSICore):

    def msi(self, path, output='./', list_files=False):
        if list_files:
            return self.call_subprocess(['{}/msiextract'.format(self.DATA_PATH), '--list', '--directory', self.get_path(output), path])
        else:
            return self.call_subprocess(['{}/msiextract'.format(self.DATA_PATH), '--directory', self.get_path(output), path])

    def stream(self, path, stream):
        return self.call_subprocess(['{}/msiinfo'.format(self.DATA_PATH), 'extract', path, stream])