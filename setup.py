# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='GramophoneTools',
    version='0.1.3',
    description='Tools for Gramophone systems by Femtonics Ltd.',
    url='http://femtonics.eu/',
    author='Femtonics Ltd.',
    author_email='info@femtonics.eu',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Programming Language :: Python :: 3.6'],
    license='GNU GPLv3',
    keywords='femtonics gramophone',
    project_urls={
        'Documentation': '',
        'User Guide': ''},
    packages=['GramophoneTools.IO', 'GramophoneTools.LinMaze', 'GramophoneTools.LinMaze.Tools', 'GramophoneTools.Recorder'],
    install_requires=[
        'h5py', 
        'PyQt5', 
        'numpy', 
        'dill', 
        'pillow', 
        'pyglet',
        'pyserial',
        'pyqtgraph',
        'matplotlib', 
        'opencv-python'],
    python_requires='>=3',
    package_data={
        'GramophoneTools.LinMaze': ['res/icon.png'],
        'GramophoneTools.Recorder': ['*.ui','*.pyw'],
        }
)
