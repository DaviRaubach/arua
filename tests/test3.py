import abjad
from abjadext import rmakers

maker = rmakers.stack(rmakers.talea([1, 1, 1], 16, extra_counts=[1]))

durations = [(1, 4), (2, 4), (3, 4), (5, 4)]

music = maker(durations)

lilypond_file = abjad.LilyPondFile.rhythm(music, durations)
# abjad.show(lilypond_file)

# print(abjad.lilypond(music))

timespan = abjad.timespan(3, 5)
expression = abjad.timespan().intersects_timespan(timespan)
print(expression(0, 10))
