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
            (r'\\absolute|\\acciaccatura|\\accidentalStyle|\\addChordShape|\\addInstrumentDefinition|\\addlyrics|\\addQuote|\\afterGrace|\\aikenHeads(Minor)?|\\allowPageTurn|\\alterBroken|\\alternative|\\appendToTag|\\applyContext|\\applyMusic|\\applyOutput|\\appoggiatura|\\ascendens|\\auctum|\\augmentum|\\autoAccidentals|\\autoBeamOff|\\autoBeamOn|\\autochange', Name.Function),
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
            (r'\\maininput|\\majorSevenSymbol|\\makeClusters|\\mark|\\markLengthOff|\\markLengthOn|\\markup|\\markuplines|\\markuplist|\\melisma|\\melismaEnd|\\mergeDifferentlyDottedOff|\\mergeDifferentlyDottedOn|\\mergeDifferentlyHeadedOff|\\mergeDifferentlyHeadedOn|\\mm|\\musicMap', Name.Function),

            # LilyPond music commands - starting with letter N
            (r'\\neumeDemoLayout|\\new|\\newSpacingSection|\\noBeam|\\noBreak|\\noPageBreak|\\noPageTurn|\\normalsize|\\notemode|\\numericTimeSignature', Name.Function),

            # LilyPond music commands - starting with letter O
            (r'\\octaveCheck|\\oldaddlyrics|\\oneVoice|\\oriscus|\\ottava|\\override|\\overrideProperty|\\overrideTimeSignatureSettings',  Name.Function),

            # LilyPond music commands - starting with letter P
            (r'\\pageBreak|\\pageTurn|\\palmMute|\\palmMuteOn|\\parallelMusic|\\parenthesisCloseSymbol|\\parenthesisOpenSymbol|\\parenthesize|\\partcombine|\\partCombineListener|\\partial|\\partialJazzExceptions|\\partialJazzMusic|\\pes|\\phrasingSlurDashed|\\phrasingSlurDotted|\\phrasingSlurDown|\\phrasingSlurNeutral|\\phrasingSlurSolid|\\phrasingSlurUp|\\pipeSymbol|\\pitchedTrill|\\pointAndClickOff|\\pointAndClickOn|\\predefinedFretboardsOff|\\predefinedFretboardsOn|\\pt|\\pushToTag', Name.Function),

            # LilyPond music commands - starting with letter Q
            (r'\\quilisma|\\quoteDuring', Name.Function),

            # LilyPond music commands - starting with letter R
            (r'\\relative|\\RemoveEmptyRhythmicStaffContext|\\RemoveEmptyStaffContext|\\removeWithTag|\\repeat|\\repeatTie|\\resetRelativeOctave|\\responsum|\\rest|\\revert|\\rightHandFinger', Name.Function),

            # LilyPond music commands - starting with letter S
            (r'\\sacredHarpHeads|\\sacredHarpHeadsMinor|\\scaleDurations|\\scoreTweak|\\semiGermanChords|\\set|\\shape|\\shiftDurations|\\shiftOff|\\shiftOn|\\shiftOnn|\\shiftOnnn|\\showStaffSwitch|\\single|\\skip|\\skipTypesetting|\\slurDashed|\\slurDotted|\\slurDown|\\slurNeutral|\\slurSolid|\\slurUp|\\small|\\sostenutoOff|\\sostenutoOn|\\southernHarmonyHeads|\\southernHarmonyHeadsMinor|\\spacingTweaks|\\startAcciaccaturaMusic|\\startAppoggiaturaMusic|\\startGraceMusic|\\startGroup|\\startStaff|\\startTextSpan|\\startTrillSpan|\\stemDown|\\stemNeutral|\\stemUp|\\stopAcciaccaturaMusic|\\stopAppoggiaturaMusic|\\stopGraceMusic|\\stopGroup|\\stopStaff|\\stopTextSpan|\\stopTrillSpan|\\stringTuning|\\strokeFingerOrientations|\\stropha|\\sustainOff|\\sustainOn', Name.Function),

            # LilyPond music commands - starting with letter T
            (r'\\tabFullNotation|\\tag|\\teeny|\\tempo|\\tempoWholesPerMinute|\\textLengthOff|\\textLengthOn|\\textSpannerDown|\\textSpannerNeutral|\\textSpannerUp|\\tieDashed|\\tieDotted|\\tieDown|\\tieNeutral|\\tieSolid|\\tieUp|\\tildeSymbol|\\time|\\times|\\timing|\\tiny|\\tocItem|\\transpose|\\transposedCueDuring|\\transposition|\\treCorde|\\tuplet|\\tupletDown|\\tupletNeutral|\\tupletUp|\\tweak', Name.Function),

            # LilyPond music commands - starting with letter U-Z
            (r'\\unaCorda|\\unfoldRepeats|\\unHideNotes|\\unit|\\unset|\\versus|\\virga|\\virgula|\\voiceFour|\\voiceFourStyle|\\voiceNeutralStyle|\\voiceOne|\\voiceOneStyle|\\voiceThree|\\voiceThreeStyle|\\voiceTwo|\\voiceTwoStyle|\\walkerHeads|\\walkerHeadsMinor|\\whiteTriangleMarkup|\\withMusicProperty', Name.Function),

            # Repeat variables
            (r'\\unfold|\\percent|\\volta|\\tremolo', Name.Variable),

            # Layout variables
            (r'indent|short-indent|system-count|line-width|ragged-right|ragged-last', Name.Variable),

            # Paper variables - fixed vertical
            (r'paper-height|top-margin|bottom-margin|ragged-bottom|ragged-last-bottom', Name.Variable),

            # Paper variables - horizontal
            (r'paper-width|line-width|left-margin|right-margin|check-consistency|ragged-right|ragged-last|two-sided|inner-margin|outer-margin|binding-offset|horizontal-shift|indent|short-indent', Name.Variable),

            # Paper variables - flex vertical
            (r'markup-system-spacing|score-markup-spacing|score-system-spacing|system-system-spacing|markup-markup-spacing|last-bottom-spacing|top-system-spacing|top-markup-spacing', Name.Variable),

            # Paper variables - line breaking
            (r'max-systems-per-page|min-systems-per-page|system-count|systems-per-page', Name.Variable),

            # Paper variables - page breaking
            (r'blank-after-score-page-force|blank-last-page-force|blank-page-force|page-breaking|         page-breaking-system-system-spacing|page-count', Name.Variable),

            # Paper variables - page numbering
            (r'auto-first-page-number|first-page-number|print-first-page-number|print-page-number', Name.Variable),

            # Paper variables - misc
            (r'page-spacing-weight|print-all-headers|system-separator-markup', Name.Variable),
    
            # Paper variables - debugging
            (r'annotate-spacing', Name.Variable),
    
            # Paper variables - different markups
            (r'bookTitleMarkup|evenFooterMarkup|evenHeaderMarkup|oddFooterMarkup|oddHeaderMarkup|scoreTitleMarkup|tocItemMarkup|tocTitleMarkup', Name.Variable),

            # Paper variables - fonts
            (r'fonts', Name.Variable),

            # Paper variables
            # undocumented?
            #'blank-after-score-page-force',
            #'force-assignment',
            #'input-encoding',
            #'output-scale',
            
            # parser variable
            (r'\\afterGraceFraction', Name.Variable),
    

            
        ],
    }
