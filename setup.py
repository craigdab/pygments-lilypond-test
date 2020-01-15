from setuptools import setup

lexers = [
    'lilypond   = lilypond:LilyPondLexer',
]

setup(
    name='pygments-lilypond',
    version='0.0.1',
    description='LilyPond Lexer for Pygments',
    long_description=__doc__,
    author='craigdab',
    author_email='craig.dabelstein@gmail.com',
    license='MIT',
    keywords='syntax highlighting lilypond',
    url='https://github.com/craigdab/pygments-lilypond-test',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    packages=['lilypond'],
    install_requires=['Pygments >= 2'],
    include_package_data=False,
    platforms=['any'],
    entry_points={
        'pygments.lexers': [
            'LilyPondLexer = lilypond:LilyPondLexer',
        ],
        'pygments.styles': [
            'lilypond = lilypond:LilyPondStyle',
        ],
    },
    zip_safe=False
)
