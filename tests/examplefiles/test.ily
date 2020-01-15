\version "2.19.16"

\include "dynamics-defs.ily"

altosaxINotesXI = \transpose c' bf {
  \relative c' {
    \clef "treble"

    %1-8
    R1*8 |

    %{
this is a block comment
    %}

    %9
    r2 e' \f |

    %10
    c2 a |

    %11
    f1 ( |

    %12
    e4 d c b |

    %13
    a4 b c ds |

    %14
    e4 ) fs ( g e |

    %15
    a4 g fs e |

    %16
    ds1 |

    %17
    e4 ) gs ( a b |

    %18
    g4 ) r r2 |

    %19
    r2 d' ( |

    %20
    b2 e4 d |

    %21
    c4 ) r a2 ~ \f |

    %22
    a4 g fs e |

    %23
    f1 ~ ( |

    %24
    f4 e d c |

    %25
    a4 b c a ) |

    %26
    b1 ( |

    %27
    c4 d e c ) |

    %28
    d1 ( |

    %29
    c2 ) r |

    %30
    R1 |

    %31
    r4 d ( g f |

    %32
    e4 ) r c'2 \f |

    %33
    b2 g |

    %34
    e'1 ( |

    %35
    d4 c b a |

    %36
    g4 ) g ( a b |

    %37
    c4 ) c ( d e |

    %38
    f4 d e f |

    %39
    g4 ) g, ( a b |

    %40
    c4 ) r c2 \f |

    %41
    a2 f |

    %42
    d'1 ( |

    %43
    c4 bf a g |

    %44
    f4 ) f' ( d c |

    %45
    b2. ) b4 (

    %46
    a4 g f e |

    %47
    d2. ) d4 |

    %48
    c4 ( \ff d e f |

    %49
    e4 f e d ) |

    %50
    c4 ( d e f |

    %51
    e4 f e d ) |

    %52
    c1 |

    %53
    d1 |

    %54
    d2. bf4 |

    %55
    c1 |

    %56
    a4 ( b c d |

    %57
    e2 ) e |

    %58
    d2 d |

    %59
    e4 ( f g a |

    %60
    g4 a g f ) |

    %61
    e4 ( f g a |

    %62
    g4 a g f ) |

    %63
    e4 ( f g a |

    %64
    g2 ) d ~ ( |

    %65
    d4 e f g |

    %66
    f2 ) c' ~ ( |

    %67
    c4 b c d |

    %68
    e4 ) b ( c d |

    %69
    e4 ) b ( c d |

    %70
    e4 ) a, ( b c |

    %71
    d4 ) gs, ( a b |

    %72
    c4 ) cs ( d e |

    %73
    f4 ) f ( e d |

    %74
    c2 ) e |

    %75
    d2 d |

    %76
    e4 ( f g e ) |

    %77
    f1 |

    %78
    e4 ( f g e ) |

    %79
    f1 ( |

    %80
    e4 ) r c2 ~ \ff |

    %81
    c2 bf ( |

    %82
    a4 ) r a ( b |

    %83
    cs4 d e cs |

    %84
    d4 e f d |

    %85
    e1 ) |

    %86
    d4 ( e f d |

    %87
    e1 |

    %88
    d4 ) r d,2 ~ \ff |

    %89
    d2 c |

    %90
    b4 ( cs ds e |

    %91
    fs4 g a fs |

    %92
    g4 ) r r2 |

    %93-95
    R1*3 |

    %96
    r2 a \f |

    %97
    c2 e |

    %98
    gs,1 ( |

    %99
    a4 b c cs |

    %100
    d4 ) r r2 |

    %101
    r4 a ( f d |

    %102
    e4 f g a ) |

    %103
    f'4 ( e d c |

    %104
    bf4 c bf a |

    %105
    g1 ) |

    %106
    r2 d' ~ |

    %107
    d4 fs g2 ~ |

    %108
    g4 r c,2 \f |

    %109
    ef2 g ( |

    %110
    af4 g f ef ) |

    %111
    d2 f (

    %112
    g4 f ef d ) |

    %113
    c2 ef ( |

    %114
    f4 ef d c ) |

    %115
    b2 d |

    %116
    ef4 r r2 |

    %117
    r2 c ~ \f |

    %118
    c2 bf4 ( a |

    %119
    g4 a bf g |

    %120
    d'4 ) r r2 |

    %121
    r2 d ~ \f |

    %122
    d2 c4 ( b |

    %123
    a4 b c a |

    %124
    e4 ) r r2 |

    %125
    R1 |

    %126
    r2 e' \f |

    %127
    c2 a |

    %128
    gs4 ( e fs gs |

    %129
    a4 b c a ) |

    %130
    b4 ( gs a b |

    %131
    c4 d e c |

    %132
    b2 ) r |

    %133
    e1 ~ \f |

    %134
    e2 d4 ( c |

    %135
    b4 c d2 ~ |

    %136
    d2 ) c4 ( b |

    %137
    a4 b c2 ~ |

    %138
    c2 ) b4 ( a |

    %139
    gs4 a b2 ~ |

    %140
    b2 ) a4 ( gs |

    %141
    a1 ~ |

    %142
    a4 ) gs ( a b |

    %143
    c1 ~ |

    %144
    c4 ) a ( c e |

    %145
    ds1 ~ |

    %146
    ds4 ) ds ( e es |

    %147
    fs1 ~ |

    %148
    fs4 ) e ( ds e |

    %149
    fs1 ~ |

    %150
    fs4 ) e ( ds e |

    %151
    fs4 e ) ds2 |

    %152
    d2 -> c -> |

    %153
    b2 -> a -> |

    %154
    gs2 -> a -> |

    %155
    gs2 -> b |

    %156
    a4 ( b c d ) |

    %157
    c4 ( d c b ) |

    %158
    a4 ( b c d ) |

    %159
    c4 ( d c b ) |

    %160
    a1 |

    %161
    b1 |

    %162
    b2. g4 |

    %163
    a1 |

    %164
    f4 ( gs a b |

    %165
    c2 ) c |

    %166
    b2 b |

    %167
    c4 ( d e f ) |

    %168
    e4 ( f e d ) |

    %169
    c4 ( d e f ) |

    %170
    e4 ( f e d ) |

    %171
    c4 ( d e fs |

    %172
    e2 ) b ~ |

    %173
    b4 cs ( d e |

    %174
    d2 ) a ~ |

    %175
    a4 gs ( a b |

    %176
    c4 ) gs ( a b |

    %177
    c4 ) gs ( a b |

    %178
    c4 ) cs ( d e |

    %179
    f4 ) b, ( c d |

    %180
    e4 ) a, ( b c |

    %181
    d4 ) gs, ( a b |

    %182
    c4 ) r cs2 \f |

    %183
    d2 ds |

    %184
    e4 r r2 |

    %185
    d4 r r2 |

    %186
    c4 \fff ^"sostenuto" c2 c4 ~ |

    %187
    c4 c2 c4 |

    %188
    d4 d2 d4 ~ |

    %189
    d4 d2 d4 |

    %190
    e4 e2 e4 ~ |

    %191
    e4 e2 e4 |

    %192
    f4 c2 c4 ~ |

    %193
    c4 c2 c4 ~ |

    %194
    c4 c2 c4 ~ |

    %195
    c4 c2 c4 ~ |

    %196
    c4 e2 c4 ~ |

    %197
    c4 e2 c4 |

    %198
    b4 d2 b4 ~ |

    %199
    b4 d2 b4 |

    %200
    c4

    <<
      {
        s4 s2 |

        %201
        s4
      }
      \new CueVoice {
        a,4 ( ^"T. Chor." c d ) |
        e4
      }
    >>

    b' \f b b |

    %202
    c4

    <<
      {
        s4 s2 |

        %201
        s4
      }
      \new CueVoice {
        a,4 ( c d ) |
        e4
      }
    >>

    b' b b |

    %204
    c4
    <<
      {
        s4 s4
      }
      \new CueVoice {
        c,4 e
      }
    >>

    a |

    %205
    gs4

    <<
      {
        s4 s4
      }
      \new CueVoice {
        gs,4 gs
      }
    >>

    gs' |

    %206
    a4
    <<
      {
        s4 s4
      }
      \new CueVoice {
        a,4 a
      }
    >>
    a' |

    %207
    gs4
    <<
      {
        s4 s4
      }
      \new CueVoice {
        gs,4 gs
      }
    >>
    e' |

    %208
    cs1 ~ \ff |

    %209
    cs1 |

    %210
    d1 ~ |

    %211
    d1 |

    %212
    d1 |

    %213
    cs2 b |

    %214
    cs1 ~ |

    %215
    cs1 \fermata

  }
}