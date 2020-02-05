from setuptools import setup, find_packages
import os
import re

# the current directory - setup.py
HERE = os.path.abspath(os.path.dirname(__file__))

def parse_req_line(line):
    line = line.strip()
    if not line or line[0] == '#':
        return None
    return line

def load_requirements(file_name):
    with open(file_name) as fp:
        reqs = filter(None, (parse_req_line(line) for line in fp))
        return list(reqs)

def find_version(distributionname):

    versionfile = '{}/{}/version.py'.format(HERE, distributionname)

    with open(versionfile) as fp:
        versiondata = fp.read()

    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", versiondata, re.M)

    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


install_requires = load_requirements('requirements.txt')

setup(
    name='tasks',
    version='find_version(tasks)',
    packages=find_packages(exclude=['tests','docs','work','logs']),
    entry_points={
        'console_scripts': [
            'tasks = tasks.work.__main__:main',
        ]
    },
    install_requires=install_requires,
    description='Tasks',
    long_description='Tasks',
    long_description_content_type='text/markdown',
    license='MIT',
    maintainer='Unknown',
    maintainer_email='example@example.com',
    url='https://github.com/example/tasks',
)
