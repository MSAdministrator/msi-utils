from .msicore import MSICore


class MSIDiff(MSICore):

    def tables(self, path):
        return self.call_subprocess(['{}/msidiff'.format(self.DATA_PATH), '--tables', path])

    def files(self, path):
        return self.call_subprocess(['{}/msidiff'.format(self.DATA_PATH), '--list', path])
        
