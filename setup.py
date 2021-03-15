from setuptools import setup, find_packages

def parse_requirements(requirement_file):
    with open(requirement_file) as f:
        return f.readlines()

setup(
    name='msi-utils',
    version='0.0.4',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Python package to assist with analzying and extracting data from a Windows Installer MSI',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=parse_requirements('./requirements.txt'),
    keywords=['carcass'],
    url='https://github.com/MSAdministrator/msiutils',
    author='MSAdministrator',
    author_email='rickardja@live.com',
    python_requires='>=3.6, <4',
    entry_points={
          'console_scripts': [
              'msi-utils = msiutils.__main__:main'
          ]
    },
    include_package_data=True,
    package_data={
        'msiutils': ['data/*']
    }
)