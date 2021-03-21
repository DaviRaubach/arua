from a_rua_dos_cataventos.components.pitch import pitches_01 as pitch
from a_rua_dos_cataventos.components.rhythm import rmakers_01 as rhythm
from a_rua_dos_cataventos.components.timespans import timespans_01 as timespans

import abjad

import muda


time_signatures = timespans.time_signatures

pitches = abjad.PitchSegment("c'")

# ALTO FLUTE
# create material
material_aflute = muda.Material("AltoFlute_Voice_1")

material_aflute.AlternatingMaterials(
    timespans.durations_aflute,  # annotate divisions
    rhythm.rmaker_afluteA,
    rhythm.rmaker_afluteB,
    rhythm.rmaker_afluteC,
    rhythm.rmaker_afluteD,
    rhythm.rest_maker,
)

# write rhythm and silences
# material_aflute.SilenceAndRythmMaker(
#     maker=rhythm.rmaker_aflute,
#     annotated_divisions=timespans.durations_aflute
# )
# write pitches
material_aflute.WritePitchesByDurations(pitch.pitches_aflute, timespans.durations_aflute)
# delete, insert before write indicators
# del material_aflute.container[-2:]
# write indicators
material_aflute.WriteIndicators(
    # which leaf receive the indicator
    # see leaves number
    # see_leaves_number=True,
    # dynamics
    # dynamic_list=["p", "mf", "f", "p < f"],
    # attach_dyn_lists=[[0], [1], [2], [(8, 10), (29, 31)]],
    # # slurs
    # slur_up=[(0, 2), (8, 10), (14, 16)],
    # slur_down=[(43, 45)],
)
# material_aflute = material_aflute.MakeMaterial()

# BASS CLARINET
# create material
material_bclarinet = muda.Material("BassClarinet_Voice_1")

# write alternated materials
material_bclarinet.AlternatingMaterials(
    timespans.durations_bclarinet,  # annotate divisions
    rhythm.rmaker_bclarinetA,
    rhythm.rmaker_bclarinetB,
    rhythm.rmaker_bclarinetC,
    rhythm.rmaker_bclarinetD,
    rhythm.rest_maker,
)
material_bclarinet.WritePitchesByDurations(pitch.pitches_bclarinet, timespans.durations_bclarinet)

material_bclarinet.WriteIndicators()

# PIANO1
material_piano1 = muda.Material("Piano_Voice_1")
material_piano1.AlternatingMaterials(
    timespans.durations_piano,  # annotate divisions
    rhythm.rmaker_piano1A,
    rhythm.rmaker_piano1B,
    rhythm.rest_maker,
)
material_piano1.WritePitches(pitches)
material_piano1.WriteIndicators()
# PIANO2
material_piano3 = muda.Material("Piano_Voice_3")
material_piano3.AlternatingMaterials(
    timespans.durations_piano,  # annotate divisions
    rhythm.rmaker_piano3A,
    rhythm.rmaker_piano3B,
    rhythm.rest_maker,
)
material_piano3.WritePitches(pitches)
material_piano3.WriteIndicators()

# VIOLIN
material_violin = muda.Material("Violin_Voice_1")
material_violin.AlternatingMaterials(
    timespans.durations_strings,  # annotate divisions
    rhythm.rmaker_violinA,
    rhythm.rmaker_violinB,
    rhythm.rest_maker,
)
material_violin.WritePitches(pitches)
material_violin.WriteIndicators()

# VIOLA
material_viola = muda.Material("Viola_Voice_1")
material_viola.AlternatingMaterials(
    timespans.durations_strings,  # annotate divisions
    rhythm.rmaker_violaA,
    rhythm.rmaker_violaB,
    rhythm.rest_maker,
)
material_viola.WritePitches(pitches)
material_viola.WriteIndicators()

# CELLO
material_cello = muda.Material("Cello_Voice_1")
material_cello.AlternatingMaterials(
    timespans.durations_strings,  # annotate divisions
    rhythm.rmaker_celloA,
    rhythm.rmaker_celloB,
    rhythm.rest_maker,
)
material_cello.WritePitches(pitches)
material_cello.WriteIndicators()
materials_list = [
    material_aflute,
    material_bclarinet,
    # material_piano1,
    # material_piano3,
    # material_violin,
    # material_viola,
    # material_cello,
]


if __name__ == "__main__":
    # show the material you are working on
    mat = material_aflute
    mat_voice = abjad.Voice(name=mat.name)
    mat_voice.append(mat.container)
    selection = abjad.select(mat_voice).leaves()
    abjad.attach(abjad.Clef("bass"), selection[0])
    skips = abjad.Voice(name="Global_Context")
    mat_staff = abjad.Staff([mat_voice, skips], simultaneous=True)
    score = abjad.Score()
    score.append(mat_staff)
    muda.functions.MakeSkips(score, time_signatures)
    muda.functions.RewriteMeter(score, time_signatures)
    abjad.show(score)
    abjad.play(score)

