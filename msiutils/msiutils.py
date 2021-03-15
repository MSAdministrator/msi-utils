from .dump import MSIDump
from .extract import MSIExtract
from .msiinfo import MSIInfo


class MSIUtils:

    @property
    def dump(self):
        return MSIDump()

    @property
    def extract(self):
        return MSIExtract()

    @property
    def get(self):
        return MSIInfo()
