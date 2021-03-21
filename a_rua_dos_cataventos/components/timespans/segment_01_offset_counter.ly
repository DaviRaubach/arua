\version "2.22.0"   %! abjad.LilyPondFile._get_format_pieces()
\language "english" %! abjad.LilyPondFile._get_format_pieces()

\markup { \overlay {
\postscript #"
0.2 setlinewidth
[ 2 1 ] 0 setdash
1 -1 moveto
0 -2 rlineto
stroke
105.99999999999999 -1 moveto
0 -2 rlineto
stroke"
\translate #'(1.0 . 1)
\sans \fontsize #-3 \center-align \fraction 0 1
\translate #'(105.99999999999999 . 1)
\sans \fontsize #-3 \center-align \fraction 35 2
} }