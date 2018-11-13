from distutils.cmd import Command
from setuptools import setup, find_packages

from download_data import main


class DownloadAll(Command):
    description = 'Download all games from game.json'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        main()


class StartServer(Command):
    description = 'Start server'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        pass


with open('README.rst', 'r') as f:
    long_desc = f.read()


setup(
    name='DOS game in browser',
    version='0.1',
    packages=find_packages(),
    scripts=[],
    install_requires=['django>=2.1.3'],
    include_package_data=True,
    package_data={
        'img': ['*'],
        '': ['README.rst', 'games.json', 'LICENSE']
    },
    cmdclass={
        'download_all': DownloadAll,
        'start_server': StartServer,
    },
    python_requires='>=3.4.0',
    author='Ray Zhu',
    description='Just an exercise',
    long_description=str(long_desc),
    license='GPL-3',
)
