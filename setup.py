from setuptools import setup, find_packages

from runpy import run_path

# Get the version from the relevant file
d = run_path('mathtools/_version.py')
__version__ = d['__version__']

# Get the development status from the version string
if 'a' in __version__:
    devstatus = 'Development Status :: 3 - Alpha'
elif 'b' in __version__:
    devstatus = 'Development Status :: 4 - Beta'
else:
    devstatus = 'Development Status :: 5 - Production/Stable'


setup(
    name="mathtools",
    version=__version__,
    packages=find_packages(),
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['numpy>=1.11', 'matplotlib>=1.5', 'h5py>=3.6.0',
        'ipython>=8.0.1'],
    # metadata for upload to PyPI
    author = "Remi Chassagne",
    author_email = "remi.chassagne@univ-grenoble-alpes.fr",
    description = "Math Processing Python Tools",
    license = 'GPLv2',
    keywords = ["Math"],
    url = "",   # project home page, if any
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        devstatus,
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        # actually CeCILL License (GPL compatible license for French laws)
        #
        # Specify the Python versions you support here. In particular,
        # ensure that you indicate whether you support Python 2,
        # Python 3 or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
        ])

