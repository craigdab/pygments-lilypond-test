import re
from pygments.lexer import RegexLexer, include, words
from pygments.token import *

from pygments.lexers._lilypond_builtins import lilypond_keywords, lilypond_music_commands, articulations, ornaments, fermatas, instrument_scripts, repeat_scripts, ancient_scripts, modes, markupcommands, markuplistcommands, contexts, midi_instruments, scheme_values, header_variables, paper_variables, layout_variables, repeat_types, accidental_styles, clefs, break_visibility, mark_formatters



__all__ = ['LilyPondLexer']

class LilyPondLexer(RegexLexer):

    name = 'LilyPond'
    aliases = ['lilypond', 'lily']
    filenames = ['*.ly', '*.ily']

    tokens = {
        
        'root': [
            include('keywords'),

            # articulation
            (r'[-_^][_.>|!+^-]', Name.Function),

            # re_dynamic
            (r'\\[<!>]', Name.Function),
            (r'\\f{1,5}|p{1,5}', Name.Function),
            (r'mf|mp|fp|spp?|sff?|sfz|rfz', Name.Function),
            (r'cresc|decresc|dim|cr|decr', Name.Function),
            # (r'(?![A-Za-z])', Name.Function), I don't know what this does yet

            #re_duration
            (r'(\\(maxima|longa|breve)\b|(1|2|4|8|16|32|64|128|256|512|1024|2048)(?!\d))', Name.Function),
            # re_dot
            (r'\.', Name.Function),

            # re_scaling
            (r'\*[\t ]*\d+(/\d+)?', Name.Function),

            # an identifier allowing letters and single hyphens in between
            # re_identifier
            (r'[^\W\d_]+([_-][^\W\d_]+)*', Name.Function),

            # the lookahead pattern for the end of an identifier (ref)
            # re_identifier_end
            #(r'(?![_-]?[^\W\d])', Name.Function), - not working

            # Whitespace
            (r'\s+', Text),

            # rests
            (r'[Rr](?![A-Za-z])', Text),

            # Pitch
            #(r'\b[a-z]+(\'|,)*', Text),
            (r'[a-x]+(?![A-Za-z])', Text),

            # Q(MusicItem):
            (r'q(?![A-Za-z])', Text),

            # DrumNote(MusicItem):
            (r'[a-z]+(?![A-Za-z])', Text),

            # Octave(_token.Token):
            (r'\,+|\'+', Text),

            # OctaveCheck(_token.Token):
            #r''=(,+|'+)?', Text),

            # Whole bar rests
            # (r'\bR', Text),

            # text in quotation marks
            # (r'"(.*?)"', String.Double),

            # text variables (if that's what you call them)
            #(r'[A-Za-z]*', Text),

            # curly brackets
            # (r'\{|\}', Punctuation),

            # double angle brackets
            # (r'<<|>>', Text),

            # equals sign
            # (r'\=', Text),

            # pipe symbol, bar check, bar number check
            # (r'\|', Text),
            #(r'\\barNumberCheck\s\#\d+', Text),

            # direction indicator
            # (r'\_|\^', Text),
    
            # Comments
            (r'%{.%}', Comment.Multiline),
            (r'%.*?\n', Comment.Singleline),

            # Dynamics
            #(r'\\!', Name.Function),
            #(r'\\f{1,5}\b|\\p{1,5}\b', Name.Function),
            #(r'\\mf|\\mp|\\fp|\\sp(p)?|\\sf(f)?|\\sfp|\\sfz|\\(r)?fz', Name.Function),
            #(r'(?![A-Za-z])', Literal),
            #(r'\\crescHairpin|\\crescTextCresc|\\cr(esc)?|\\decr(esc)?|\\dim(Hairpin)?|\\dimTextDecr(esc)?|\\dimTextDim|\\endcr(esc)?|\\enddecr|\\enddim', Name.Function),
            #(r'\\<|\\>', Name.Function),

            # Articulations
            #(r'[-_^][_.>|!+^-]', Text),
            #(r'\\accent|\\espressivo|\\marcato|\\portato|\\staccatissimo|\\staccato|\\tenuto', Keyword.Reserved),

            # slurs
            (r'\(|\)', Text),

            # Duration
            #(r'\\maxima|\\longa|\\breve', Keyword.Reserved),
            #(r'(1|2|4|8|16|32|64|128|256|512|1024|2048)\.*(?!\d)', Keyword.Pseudo),

            # Scaling
            #(r'\*[\t ]*\d+(/\d+)?', Keyword.Pseudo), # Asterix #(r'\d*\*\d*', Keyword.Pseudo),
            
        ],

            'keywords': [
            (words(lilypond_music_commands, prefix = r'\\'), Name.Builtin),
            (words(lilypond_keywords, prefix = r'\\'), Name.Builtin),
            (words(articulations, prefix = r'\\'), Name.Function),
            (words(ornaments, prefix = r'\\'), Name.Function),
            (words(fermatas, prefix = r'\\'), Name.Function),
            (words(instrument_scripts, prefix = r'\\'), Name.Function),
            (words(repeat_scripts, prefix = r'\\'), Name.Function),
            (words(ancient_scripts, prefix = r'\\'), Name.Function),
            (words(modes, prefix = r'\\'), Name.Function),
            (words(markupcommands, prefix = r'\\'), Name.Function),
            (words(markuplistcommands, prefix = r'\\'), Name.Function),
            (words(contexts), Name.Variable),
            (words(midi_instruments), Name.Variable),
            (words(scheme_values), Name.Function),
            (words(header_variables), Name.Variable),
            (words(paper_variables), Name.Variable),
            (words(layout_variables), Name.Variable),
            #(words(midi_variables), Name.Variable),
            (words(repeat_types), Name.Variable),
            (words(accidental_styles), Name.Variable),
            (words(clefs), Name.Variable),
            (words(break_visibility), Name.Variable),
            (words(mark_formatters), Name.Variable),
        ],
    }
