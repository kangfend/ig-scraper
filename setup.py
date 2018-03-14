from setuptools import setup

setup(
    name='ig-scraper',
    packages=['ig_scraper'],
    version='0.0.1',
    description='Instagram hashtag scraper',
    license='MIT',
    author='Sutrisno Efendi',
    author_email='kangfend@gmail.com',
    url='https://github.com/kangfend/ig-scraper',
    download_url='https://github.com/kangfend/ig-scraper/tarball/0.0.1',
    keywords=['Instagram', 'Scraper'],
    install_requires=['requests==2.18.4'],
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