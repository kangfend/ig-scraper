from setuptools import setup
from ig_scraper import __version__


__author__ = 'Sutrisno Efendi <kangfend@gmail.com>'


setup(
    name='ig-scraper',
    packages=['ig_scraper'],
    version=__version__,
    description='Instagram hashtag scraper',
    license='MIT',
    author='Sutrisno Efendi',
    author_email='kangfend@gmail.com',
    url='https://github.com/kangfend/ig-scraper',
    download_url='https://github.com/kangfend/ig-scraper/tarball/' + __version__,  # noqa
    keywords=['Instagram', 'Scraper'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
