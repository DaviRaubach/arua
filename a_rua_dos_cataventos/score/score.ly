\version "2.22.0"
\language "english"
#(set-global-staff-size 13)


#(ly:set-option 'relative-includes #t)
\include "/Users/Davi/github/my_venv_modules/abjad/docs/source/_stylesheets/abjad.ily"
\include "/Users/Davi/Composição/2021/a_rua_dos_cataventos/a_rua_dos_cataventos/score/stylesheet.ily"

\score {
  {
    \include "segment_00.ly"
    \include "segment_01.ly"
  }
  \layout { }
  \midi { }

}
