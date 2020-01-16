import re
from pygments.lexer import RegexLexer, bygroups
from pygments.token import Keyword, Number, Text, Comment, Name

__all__ = ['LilyPondLexer']


class LilyPondLexer(RegexLexer):

    name = 'LilyPond'
    aliases = ['lilypond', 'lily']
    filenames = ['*.ly', '*.ily']

    tokens = {
        'root': [
            # Whitespace
            (r'\s', Text),

            # LilyPond Keywords
            (r'\\version|\\accepts|\\alias|\\consists|\\defaultchild|\\denies|\\hide|\\include|\\language|\\name|\\omit|\\once|\\set|\\unset|\\override|\\revert|\\remove|\\temporary|\\undo|\\score|\\book|\\bookpart|\\header|\\paper|midi|\\layout|\\with|\\context', Keyword.Reserved),
            # Lilypond Keywords commented out in python-ly/ly/words.py
            #'description',#'grobdescriptions',#'invalid',#'objectid',#'sequential',#'simultaneous',#'type',
    
            # Comments
            (r'%{.%}', Comment.Multiline),
            (r'%.*\n', Comment.Singleline),

            # Dynamics
            #(r'\\[<!>]|', Literal),
            #(r'\\f{1,5}|p{1,5}', Literal),
            #(r'|mf|mp|fp|spp?|sff?|sfz|rfz', Literal),
            #(r'|cresc|decresc|dim|cr|decr', Literal),
            #(r'(?![A-Za-z])', Literal),

            # Articulations
            #(r'[-_^][_.>|!+^-]', Literal),
            (r'\\accent|\\espressivo|\\marcato|\\portato|\\staccatissimo|\\staccato|\\tenuto', Keyword.Reserved),

            # Duration
            (r'\\maxima|\\longa|\\breve', Keyword.Reserved),
            #(r'\b|1|2|4|8|16|32|64|128|256|512|1024|2048(?!\d)', Keyword.Pseudo), NOT WORKING YET

            # Dot
            #(r'\.', Punctuation),

            # Fermatas
            (r'\\shortfermata|\\fermata|\\longfermata|\\verylongfermata', Keyword.Reserved),

            # Ornaments
            (r'\\prall|\\mordent|\\prallmordent|\\turn|\\upprall|\\downprall|\\upmordent|\\downmordent|\\lineprall|\\prallprall|\\pralldown|\\prallup|\\reverseturn|\\trill', Keyword.Reserved),

            # Instrument Scripts
            (r'\\upbow|\\downbow|\\flageolet|\\thumb|\\snappizzicato|\\open|\\halfopen|\\stopped|\\lheel|\\rheel|\\ltoe|\\rtoe', Keyword.Reserved),

            # Repeat Scripts
            (r'\\segno|coda|varcoda', Keyword.Reserved),

            # Ancient Scripts
            (r'\\ictus|\\accentus|\\circulus|\\semicirculus|\\signumcongruentiae', Keyword.Reserved),

            # Modes
            (r'\\major|\\minor|\\ionian|\\dorian|\\phrygian|\\lydian|\\mixolydian|\\aeolian|\\locrian', Keyword.Reserved),  

            # Contexts
            (r'\\ChoirStaff|\\ChordNames|\\CueVoice|\\Devnull|\\DrumStaff|\\DrumVoice|\\Dynamics|\\FiguredBass|\\FretBoards|\\Global|\\GrandStaff|\\GregorianTranscriptionStaff|\\GregorianTranscriptionVoice|\\KievanStaff|\\KievanVoice|\\Lyrics|\\MensuralStaff|\\MensuralVoice|\\NoteNames|\\NullVoice|\\PetrucciStaff|\\PetrucciVoice|\\PianoStaff|\\RhythmicStaff|\\Score|\\Staff|\\StaffGroup|\\TabStaff|\\TabVoice|\\Timing|\\VaticanaStaff|\\VaticanaVoice|\\Voice', Keyword.Reserved),


            # Scaling
            # (r'\*[\t ]*\d+(/\d+)?', Scaling)

            # lilypond music commands
            (r'\\absolute|acciaccatura|accidentalStyle|addChordShape|addInstrumentDefinition|addlyrics|addQuote|afterGrace', Name.Function), 

            # parser variable
            (r'\\afterGraceFraction', Name.Variable),
    

            
        ],
    }
