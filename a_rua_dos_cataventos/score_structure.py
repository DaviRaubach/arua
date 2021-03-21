import abjad
import muda


# Create instruments
alto_flute = muda.Instrument(
    abjad_instrument=abjad.AltoFlute(),
    lilypond_name="AltoFlute",
    nstaffs=1,
    nvoices=[1],
)

# Note: the markup for "instrumentName" in lilypond will be the lilypond_name variable with a espace between the words.
bass_clarinet = muda.Instrument(
    abjad_instrument=abjad.BassClarinet(),
    lilypond_name="BassClarinet",
    nstaffs=1,
    nvoices=[1],
)
piano = muda.Instrument(
    abjad_instrument=abjad.Piano(),
    lilypond_name="Piano",
    nstaffs=2,
    nvoices=[2, 2],
    piano=True,
)
violin = muda.Instrument(
    abjad_instrument=abjad.Violin(), lilypond_name="Violin", nstaffs=1, nvoices=[1]
)
viola = muda.Instrument(
    abjad_instrument=abjad.Viola(), lilypond_name="Viola", nstaffs=1, nvoices=[1]
)
cello = muda.Instrument(
    abjad_instrument=abjad.Cello(), lilypond_name="Cello", nstaffs=1, nvoices=[1]
)
instruments = [alto_flute, bass_clarinet, piano, violin, viola, cello]

# Create score
score = muda.Score()

# Add instruments to score
score.AddInstrument(instruments)
