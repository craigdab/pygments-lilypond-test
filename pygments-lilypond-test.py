from pygments.lexer import RegexLexer
from pygments.token import *

class LilyPondLexer(RegexLexer):
    name = 'LilyPond'
    aliases = ['ly', 'ily']
    filenames = ['*.ly', '*.ily']

    tokens = {
        'root': [
        (r'%{.%}', Comment.Multiline),
        (r'%.*\n', Comment.Singleline),
        (r'\\[<!>]|', Dynamic),
        (r'\\(f{1,5}|p{1,5}', Dynamic),
        (r'|mf|mp|fp|spp?|sff?|sfz|rfz', Dynamic),
        (r'|cresc|decresc|dim|cr|decr', Dynamic),
        (r')(?![A-Za-z])', Dynamic),
        (r'[-_^][_.>|!+^-]', Articulation),
        (r'(\\(maxima|longa|breve)\b|(1|2|4|8|16|32|64|128|256|512|1024|2048)(?!\d))', Duration),
        (r'\.', Dot),
        (r'\*[\t ]*\d+(/\d+)?', Scaling)
        ]
    }
