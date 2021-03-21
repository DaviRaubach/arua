import abjad

chord_01 = abjad.PitchSegment(
    "af'' g'' fs'' "
    + "f'' d'' cs'' "
    + "b'' af'' g'' "
    + "e'' c'' g'' "
    + "fs'' cs'' gs''",
)

chord_02 = abjad.PitchSegment(
    "af'' g'' fs'' "
    + "f'' d'' cs'' "
    + "b'' af'' g'' "
    + "e'' c'' g'' "
    + "fs'' cs'' gs''"
)

pitches_aflute = {
    "aflute_A": abjad.PitchSegment([-5, -3, 0]),
    "aflute_B": abjad.PitchSegment([4, 5]),
    "aflute_C": abjad.PitchSegment([2, 4]),
    "aflute_D": abjad.PitchSegment([0, -2]),
}

pitches_bclarinet = {
    "bclarinet_A": abjad.PitchSegment([-10, -17, -19]),
    "bclarinet_B": abjad.PitchSegment([-22, -19]),
    "bclarinet_C": abjad.PitchSegment([-17, -15]),
    "bclarinet_D": abjad.PitchSegment([-12, -8]),
}


# pitches_bclarinet = abjad.PitchSegment([-10, -17, -19, -22, -19, -17, -15, -12])

pitch_list_01 = [
    chord_01,
    chord_02,
    chord_01,
    chord_02,
    chord_01,
    chord_02,
    chord_01,
]
