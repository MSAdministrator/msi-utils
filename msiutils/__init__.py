import os

data_path = os.path.join(os.path.dirname(__file__), 'data')
for item in os.listdir(data_path):
    if not os.access(os.path.join(data_path, item), os.X_OK):
        os.chmod(os.path.join(data_path, item), 0o777)

from .msiutils import MSIUtils