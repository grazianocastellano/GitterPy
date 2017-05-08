from distutils.core import setup

import gitter

version = gitter.__version__

setup_kwargs = {
    'name': 'gitter',
    'version': version,
    'url': 'https://github.com/MichaelYusko/GitterHQPy',
    'license': 'GNU',
    'author': 'Fresh Jelly',
    'author_email': 'freshjelly12@yahoo.com',
    'description': 'Python interface for the Gitter API',
    'packages': ['gitter'],
    'classifiers': [
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: GNU General Public License (GPL)'
    ],
 }

requirements = ['requests>=2.13.0']
setup_kwargs['install_requires'] = requirements

setup(**setup_kwargs)

print(u"\n\n\t\t    "
      "GitterHQPy version {} installation succeeded.\n".format(version))
