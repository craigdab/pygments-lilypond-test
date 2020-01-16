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
            (r'\\f{1,5}\s|p{1,5}\s', Name.Function), #added a space after the dynamic to make it work but this is probably not the right way
            (r'\\mf|\\mp|\\fp|\\sp|\\spp|\\sf|\\sff|\\sfp|\\sfz|\\rfz|\\fz', Name.Function),
            #(r'(?![A-Za-z])', Literal),
            (r'\\cr|\\cresc|\\crescHairpin|\\crescTextCresc|\\decr|\\decresc|\\dim|\\dimHairpin|\\dimTextDecr|\\dimTextDecresc|\\dimTextDim|\\endcr|\\endcresc|\\enddecr|\\enddim', Name.Function),

            # Articulations
            #(r'[-_^][_.>|!+^-]', Literal),
            (r'\\accent|\\espressivo|\\marcato|\\portato|\\staccatissimo|\\staccato|\\tenuto', Keyword.Reserved),

            # Duration
            (r'\\maxima|\\longa|\\breve', Keyword.Reserved),
            #(r'\b|1|2|4|8|16|32|64|128|256|512|1024|2048(?!\d)', Keyword.Pseudo), NOT WORKING YET

            # Dot
            #(r'\.', Punctuation),

            # Fermatas
            (r'\\shortfermata|\\fermata|\\longfermata|\\verylongfermata|\\fermataMarkup', Keyword.Reserved), # clash with fermata and fermataMarkup

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

            # Header Variables
            (r'dedication|title|subtitle|subsubtitle|poet|composer|meter|opus|arranger|instrument|piece|breakbefore|copyright|tagline|mutopiatitle|mutopiacomposer|mutopiapoet|mutopiaopus|mutopiainstrument|date|enteredby|source|style|maintainer|maintainerEmail|maintainerWeb|moreInfo|lastupdated|texidoc|footer', Keyword.Reserved),


            # Scaling
            #(r'\*[\t ]*\d+(/\d+)?', Scaling)

            # LilyPond music commands - starting with letter A
            (r'\\absolute|\\acciaccatura|\\accidentalStyle|\\addChordShape|\\addInstrumentDefinition|\\addlyrics|\\addQuote|\\afterGrace|\\aikenHeads|\\aikenHeadsMinor|\\allowPageTurn|\\alterBroken|\\alternative|\\appendToTag|\\applyContext|\\applyMusic|\\applyOutput|\\appoggiatura|\\arpeggio|\\arpeggioArrowDown|\\arpeggioArrowUp|\\arpeggioBracket|\\arpeggioNormal|\\arpeggioParenthesis|\\ascendens|\\auctum|\\augmentum|\\autoAccidentals|\\autoBeamOff|\\autoBeamOn|\\autochange', Name.Function),
            #'AncientRemoveEmptyStaffContext',
                
            # LilyPond music commands - starting with letter B   
            (r'\\balloonGrobText|\\balloonLengthOff|\\balloonLengthOn|\\balloonText|\\bar|\\barNumberCheck|\\bassFigureExtendersOff|\\bassFigureExtendersOn|\\bassFigureStaffAlignmentDown|\\bassFigureStaffAlignmentNeutral|\\bassFigureStaffAlignmentUp|\\bendAfter|\\blackTriangleMarkup|\\bookOutputName|\\bookOutputSuffix|\\bracketCloseSymbol|\\bracketOpenSymbol|\\break|\\breathe', Name.Function),

            # LilyPond music commands - starting with letter C   
            (r'\\cadenzaOff|\\cadenzaOn|\\caesura|\\cavum|\\change|\\chordmode|\\chordRepeats|\\chords|\\clef|\\cm|\\compoundMeter|\\compressFullBarRests|\\context|\\crossStaff|\\cueClef|\\cueClefUnset|\\cueDuring|\\cueDuringWithClef', Name.Function),
            #'chordNameSeparator', #'chordPrefixSpacer', #'chordRootNamer',

            # LilyPond music commands - starting with letter D
            (r'\\dashBar|\\dashDash|\\dashDot|\\dashHat|\\dashLarger|\\dashPlus|\\dashUnderscore|\\deadNote|\\default|\\defaultNoteHeads|\\defaultTimeSignature|\\defineBarLine|\\deminutum|\\denies|\\descendens|\\displayLilyMusic|\\displayMusic|\\divisioMaior|\\divisioMaxima|\\divisioMinima|\\dotsDown|\\dotsNeutral|\\dotsUp|\\drummode|\\drumPitchTable|\\drums|\\dynamicDown|\\dynamicNeutral|\\dynamicUp', Name.Function),

            # LilyPond music commands - starting with letter E
            (r'\\easyHeadsOff|\\easyHeadsOn|\\endincipit|\\endSpanners|\\episemFinis|\\episemInitium|\\escapedBiggerSymbol|\\escapedExclamationSymbol|\\escapedParenthesisCloseSymbol|\\escapedParenthesisOpenSymbol|\\escapedSmallerSymbol|\\expandFullBarRests', Name.Function),

            # LilyPond music commands - starting with letter F
            (r'\\featherDurations|\\figuremode|\\figures|\\finalis|\\fingeringOrientations|\\flexa|\\frenchChords|\\fullJazzExceptions|\\funkHeads|\\funkHeadsMinor', Name.Function),
    
            # LilyPond music commands - starting with letter G
            (r'\\germanChords|\\glissando|\\grace|\\graceSettings', Name.Function),

            # LilyPond music commands - starting with letter H
            (r'\\harmonic|\\hideNotes|\\hideStaffSwitch|\\huge', Name.Function),

            # LilyPond music commands - starting with letter I
            (r'\\ignatzekExceptionMusic|\\ignatzekExceptions|\\iij|\\IIJ|\\ij|\\IJ|\\improvisationOff|\\improvisationOn|\\in|\\inclinatum|\\includePageLayoutFile|\\indent|\\instrumentSwitch|\\instrumentTransposition|\\interscoreline|\\italianChords', Name.Function),

            # LilyPond music commands - starting with letter K
            (r'\\keepWithTag|\\key|\\killCues', Name.Function),

            # LilyPond music commands - starting with letter L
            (r'\\label|\\laissezVibrer|\\large|\\ligature|\\linea|\\lyricmode|\\lyrics|\\lyricsto', Name.Function),

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
