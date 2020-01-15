from setuptools import setup

meta_lexers = [
    'aterm    = metaborg.pygments.lexers.meta:ATermLexer',
    'esv      = metaborg.pygments.lexers.meta:ESVLexer',
    'nabl     = metaborg.pygments.lexers.meta:NaBLLexer',
    'nabl2    = metaborg.pygments.lexers.meta:NaBL2Lexer',
    'sdf3     = metaborg.pygments.lexers.meta:SDF3Lexer',
    'stratego = metaborg.pygments.lexers.meta:StrategoLexer',
    'dynsem   = metaborg.pygments.lexers.meta:DynSemLexer',
    'doc-lex  = metaborg.pygments.lexers.meta:DocLEXLexer',
    'doc-cf-[ = metaborg.pygments.lexers.meta:DocCFSquareLexer',
    'doc-cf-< = metaborg.pygments.lexers.meta:DocCFPointyLexer',
]

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
    url='http://github.com/rsmenon/pygments-mathematica/',
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
