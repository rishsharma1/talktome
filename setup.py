try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '',
    'author': 'Rishabh Sharma',
    'url': '',
    'download_url': '',
    'author_email': 'rishsharma13@gmail.com',
    'version': '0.1',
    'install_requires': ['nose','pyglet'],
    'packages': ['talktome'],
    'scripts': [],
    'name': 'talktome'
}

setup(**config)
