from setuptools import setup

with open('README.md') as f:
    README = f.read()

setup(
    name='plex2letterboxd',
    url='https://github.com/mtimkovich/plex2letterboxd',
    version='1.1',
    author='Max Timkovich',
    author_email='max@timkovi.ch',
    license='MIT',
    description='Export watched movies on Plex to the Letterboxd import format.',
    long_description=README,
    install_requires=['plexapi'],
    python_requires='>=3',
    entry_points={'console_scripts': [
        'plex_to_letterboxd=plex_to_letterboxd:main'
    ]},
)
