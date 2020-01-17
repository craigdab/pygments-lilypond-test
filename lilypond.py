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

            # Pitch
            (r'\b[a-z]+(\'|,)*', Text),

            # Whole bar rests
            (r'\bR', Text),

            # text in quotation marks
            (r'"(.*?)"', Text),

            # curly brackets
            (r'\{|\}', Text),

            # double angle brackets
            (r'<<|>>', Text),

            # pipe symbol, bar check, bar number check
            (r'\|', Text),
            (r'\\barNumberCheck\s\#\d+', Text),

            # direction indicator
            (r'\_|\^', Text),

            # LilyPond Keywords
            (r'\\version|\\accepts|\\alias|\\consists|\\defaultchild|\\denies|\\hide|\\include|\\language|\\name|\\omit|\\once|\\(un)?set|\\override|\\revert|\\remove|\\temporary|\\undo|\\score|\\header|\\paper|\\midi|\\layout|\\with|\\context', Keyword.Reserved),
            # Lilypond Keywords commented out in python-ly/ly/words.py
            #'description',#'grobdescriptions',#'invalid',#'objectid',#'sequential',#'simultaneous',#'type',

            # Book
            (r'\\book(part|OutputName|OutputSuffix)?', Keyword.Reserved),
    
            # Comments
            (r'%{.%}', Comment.Multiline),
            (r'%.*\n', Comment.Singleline),

            # Dynamics
            (r'\\!', Name.Function),
            (r'\\f{1,5}\b|\\p{1,5}\b', Name.Function),
            (r'\\mf|\\mp|\\fp|\\sp(p)?|\\sf(f)?|\\sfp|\\sfz|\\(r)?fz', Name.Function),
            #(r'(?![A-Za-z])', Literal),
            (r'\\crescHairpin|\\crescTextCresc|\\cr(esc)?|\\decr(esc)?|\\dim(Hairpin)?|\\dimTextDecr(esc)?|\\dimTextDim|\\endcr(esc)?|\\enddecr|\\enddim', Name.Function),
            (r'\\<|\\>', Name.Function),

            # Articulations
            (r'[-_^][_.>|!+^-]', Text),
            (r'\\accent|\\espressivo|\\marcato|\\portato|\\staccatissimo|\\staccato|\\tenuto', Keyword.Reserved),

            # slurs
            (r'\(|\)', Text),

            # Duration
            (r'\\maxima|\\longa|\\breve', Keyword.Reserved),
            (r'(1|2|4|8|16|32|64|128|256|512|1024|2048)\.*(?!\d)', Keyword.Pseudo),

            # Scaling
            (r'\*[\t ]*\d+(/\d+)?', Keyword.Pseudo), # Asterix #(r'\d*\*\d*', Keyword.Pseudo),

            # Fermatas
            (r'\\shortfermata|\\(very)?longfermata', Keyword.Reserved),
            (r'\\fermata(Markup)?', Keyword.Reserved),

            # Ornaments
            (r'\\prall(mordent|up|down|prall)?|\\(up|down)?mordent|\\(reverse)?turn|\\(up|down|line)?prall|\\trill', Keyword.Reserved),

            # Instrument Scripts
            (r'\\(up|down)?bow|\\flageolet|\\thumb|\\snappizzicato|\\(half)?open|\\stopped|\\(l|r)?heel|\\(l|r)?toe', Keyword.Reserved),

            # Repeat Scripts
            (r'\\segno|coda|varcoda', Keyword.Reserved),

            # Ancient Scripts
            (r'\\ictus|\\accentus|\\(semi)?circulus|\\signumcongruentiae', Keyword.Reserved),

            # Modes
            (r'\\major|\\minor|\\ionian|\\dorian|\\phrygian|\\lydian|\\mixolydian|\\aeolian|\\locrian', Keyword.Reserved),  

            # Contexts
            (r'ChordNames|Devnull|Dynamics|FiguredBass|FretBoards|Global|Lyrics|NoteNames|Score|StaffGroup|Timing', Keyword.Reserved),

            # Contexts -- Staff
            (r'(Choir|Drum|Grand|GregorianTranscription|Kievan|Mensural|Petrucci|Piano|Rhythmic|Tab|Vaticana)?Staff', Keyword.Reserved), 

            # Contexts -- Voice
            (r'(Cue|Drum|GregorianTranscription|Kievan|Mensural|Null|Petrucci|Tab|Vaticana)?Voice', Keyword.Reserved),

            # Header Variables
            (r'dedication|poet|composer|meter|opus|arranger|instrument|piece|breakbefore|copyright|tagline|date|enteredby|source|style|moreInfo|lastupdated|texidoc|footer', Keyword.Reserved),
            (r'(subsub|sub)?title', Keyword.Reserved), # title, subtitle, subsubtitle
            (r'mutopia(title|composer|poet|opus|instrument)?', Keyword.Reserved), #mutopia
            (r'maintainer(Email|Web)?', Keyword.Reserved), #maintainer

            # LilyPond music commands - starting with letter A
            (r'\\absolute|\\acciaccatura|\\accidentalStyle|\\addChordShape|\\addInstrumentDefinition|\\addlyrics|\\addQuote|\\afterGrace(Fraction)?|\\aikenHeads(Minor)?|\\allowPageTurn|\\alterBroken|\\alternative|\\appendToTag|\\applyContext|\\applyMusic|\\applyOutput|\\appoggiatura|\\ascendens|\\auctum|\\augmentum|\\autoAccidentals|\\autoBeamOff|\\autoBeamOn|\\autochange', Name.Function),
            # Arpeggios
            (r'\\arpeggio(ArrowDown|ArrowUp|Bracket|Normal|Parenthesis)?', Name.Function),
            #'AncientRemoveEmptyStaffContext',
                
            # LilyPond music commands - starting with letter B   
            (r'\\balloon(GrobText|LengthOff|LengthOn|Text)?|\\bar\s|\\bassFigure(ExtendersOff|ExtendersOn|StaffAlignmentDown|StaffAlignmentNeutral|StaffAlignmentUp)?|\\bendAfter|\\blackTriangleMarkup|\\bracket(Close|Open)?Symbol|\\break|\\breathe', Name.Function),

            # LilyPond music commands - starting with letter C   
            (r'\\cadenza(Off|On)?|\\caesura|\\cavum|\\change|\\chordmode|\\chordRepeats|\\chords|\\clef|\\cm|\\compoundMeter|\\compressFullBarRests|\\context|\\crossStaff|\\cueClef(Unset)?|\\cueDuring(WithClef)?', Name.Function),
            #'chordNameSeparator', #'chordPrefixSpacer', #'chordRootNamer',

            # LilyPond music commands - starting with letter D
            (r'\\dash(Bar|Dash|Dot|Hat|Larger|Plus|Underscore)?\\deadNote|\\default(NoteHeads|TimeSignature)?|\\defineBarLine|\\deminutum|\\denies|\\descendens|\\displayLilyMusic|\\displayMusic|\\divisio(Maior|Maxima|Minima)?|\\dots(Down|Neutral|Up)?|\\drummode|\\drumPitchTable|\\drums|\\dynamic(Down|Neutral|Up)?', Name.Function),

            # LilyPond music commands - starting with letter E
            (r'\\easyHeads(Off|On)?|\\endincipit|\\endSpanners|\\episem(Finis|Initium)?|\\escaped(BiggerSymbol|ExclamationSymbol|ParenthesisCloseSymbol|ParenthesisOpenSymbol|SmallerSymbol)?|\\expandFullBarRests', Name.Function),

            # LilyPond music commands - starting with letter F
            (r'\\featherDurations|\\figuremode|\\figures|\\finalis|\\fingeringOrientations|\\flexa|\\frenchChords|\\fullJazzExceptions|\\funkHeads(Minor)?', Name.Function),
    
            # LilyPond music commands - starting with letter G
            (r'\\germanChords|\\glissando|\\grace(Settings)?', Name.Function),

            # LilyPond music commands - starting with letter H
            (r'\\harmonic|\\hide(Notes|StaffSwitch)?|\\huge', Name.Function),

            # LilyPond music commands - starting with letter I
            (r'\\ignatzekException(Music)?|\\iij|\\IIJ|\\ij|\\IJ|\\improvisation(Off|On)?|\\in(clinatum)?|\\includePageLayoutFile|\\indent|\\instrument(Switch|Transposition)?|\\interscoreline|\\italianChords', Name.Function),

            # LilyPond music commands - starting with letter K
            (r'\\keepWithTag|\\key|\\killCues', Name.Function),

            # LilyPond music commands - starting with letter L
            (r'\\label|\\laissezVibrer|\\large|\\ligature|\\linea|\\lyricmode|\\lyrics(to)?', Name.Function),

            # LilyPond music commands - starting with letter M
            (r'\\maininput|\\majorSevenSymbol|\\makeClusters|\\mark(LengthOff|LengthOn)?|\\markup(lines|list)?|\\melisma(End)?|\\mergeDifferentlyDotted(Off|On)?|\\mergeDifferentlyHeaded(Off|On)?|\\mm|\\musicMap', Name.Function),

            # LilyPond music commands - starting with letter N
            (r'\\neumeDemoLayout|\\new(SpacingSection)?|\\no(Beam|Break|PageBreak|PageTurn)?|\\normalsize|\\notemode|\\numericTimeSignature', Name.Function),

            # LilyPond music commands - starting with letter O
            (r'\\octaveCheck|\\oldaddlyrics|\\oneVoice|\\oriscus|\\ottava|\\override(Property|TimeSignatureSettings)?',  Name.Function),

            # LilyPond music commands - starting with letter P
            (r'\\page(Break|Turn)?|\\palmMute(On)?|\\parallelMusic|\\parenthesis(Close|Open)?Symbol|\\parenthesize|\\partcombine|\\partCombineListener|\\partial(JazzExceptions|JazzMusic)?|\\pes|\\phrasingSlur(Dashed|Dotted|Down|Neutral|Solid|Up)?|\\pipeSymbol|\\pitchedTrill|\\pointAndClick(Off|On)?|\\predefinedFretboards(Off|On)?|\\pt|\\pushToTag', Name.Function),

            # LilyPond music commands - starting with letter Q
            (r'\\quilisma|\\quoteDuring', Name.Function),

            # LilyPond music commands - starting with letter R
            (r'\\relative|\\RemoveEmpty(Rhythmic)?StaffContext|\\removeWithTag|\\repeat(Tie)?|\\resetRelativeOctave|\\responsum|\\rest|\\revert|\\rightHandFinger', Name.Function),

            # LilyPond music commands - starting with letter S
            (r'\\sacredHarpHeads(Minor)?|\\scaleDurations|\\scoreTweak|\\semiGermanChords|\\set|\\shape|\\shift(Durations|Off|On)?|\\shiftOnn(n)?|\\showStaffSwitch|\\single|\\skip(Typesetting)?|\\slur(Dashed|Dotted|Down|Neutral|Solid|Up)?|\\small|\\sostenuto(Off|On)?|\\southernHarmonyHeads(Minor)?|\\spacingTweaks|\\start(Acciaccatura|Appoggiatura)?Music|\\start(GraceMusic|Group|Staff|TextSpan|TrillSpan)?|\\stem(Down|Neutral|Up)?|\\stop(Acciaccatura|Appoggiatura)?Music|\\stop(GraceMusic|Group|Staff|TextSpan|TrillSpan)?|\\stringTuning|\\strokeFingerOrientations|\\stropha|\\sustain(Off|On)?', Name.Function),

            # LilyPond music commands - starting with letter T
            (r'\\tabFullNotation|\\tag|\\teeny|\\tempo(WholesPerMinute)?|\\textLength(Off|On)?|\\textSpanner(Down|Neutral|Up)?|\\tie(Dashed|Dotted|Down|Neutral|Solid|Up)?|\\tildeSymbol|\\time(s)?|\\timing|\\tiny|\\tocItem|\\transpose(dCueDuring)?|\\transposition|\\treCorde|\\tuplet(Down|Neutral|Up)?|\\tweak', Name.Function),

            # LilyPond music commands - starting with letter U-Z
            (r'\\unaCorda|\\unfoldRepeats|\\unHideNotes|\\unit|\\versus|\\virga|\\virgula|\\voiceFour(Style)?|\\voiceNeutralStyle|\\voiceOne(Style)?|\\voiceThree(Style)?|\\voiceTwo(Style)?|\\walkerHeads(Minor)?|\\whiteTriangleMarkup|\\withMusicProperty', Name.Function),

            # Repeat variables
            (r'\\unfold|\\percent|\\volta|\\tremolo', Name.Variable),

            # Layout variables
            (r'(short-)?indent|system-count|line-width|ragged(-right|-last)?', Name.Variable),

            # Paper variables - fixed vertical
            (r'paper-height|(top-|bottom-)?margin|ragged(-bottom|-last-bottom)?', Name.Variable),

            # Paper variables - horizontal
            (r'(paper-|line-)?width|(left-|right-)?margin|check-consistency|ragged(-right|-last)?|two-sided|(inner-|outer-)?margin|binding-offset|horizontal-shift|(short-)?indent', Name.Variable),

            # Paper variables - flex vertical
            (r'(markup-|score-|system-)?system-spacing|(score-|markup-)?markup-spacing|last-bottom-spacing|top-(system-|markup-)?spacing', Name.Variable),

            # Paper variables - line breaking
            (r'(max-|min-)?systems-per-page|system-count|systems-per-page', Name.Variable),

            # Paper variables - page breaking
            (r'(blank-after-score|blank-last-|blank-)?page-force|page-breaking(-system-system-spacing)?|page-count', Name.Variable),

            # Paper variables - page numbering
            (r'(auto-|print-)?first-page-number|print-page-number', Name.Variable),

            # Paper variables - misc
            (r'page-spacing-weight|print-all-headers|system-separator-markup', Name.Variable),
    
            # Paper variables - debugging
            (r'annotate-spacing', Name.Variable),
    
            # Paper variables - different markups
            (r'(bookTitle|evenFooter|evenHeader|oddFooter|oddHeader|scoreTitle|tocItem|tocTitle)?Markup', Name.Variable),

            # Paper variables - fonts
            (r'fonts', Name.Variable),

            # Paper variables
            # undocumented?
            #'blank-after-score-page-force',
            #'force-assignment',
            #'input-encoding',
            #'output-scale',
    

            
        ],
    }
