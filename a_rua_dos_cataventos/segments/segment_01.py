# -*- coding: utf-8 -*-
# This file adds materials to voices and generate a segment

import os
import abjad
import muda
from a_rua_dos_cataventos.score_structure import score
from a_rua_dos_cataventos.materials import materials_01 as materials


# SEGMENT 01
score.MakeSkips(materials.time_signatures)
score.WriteMaterials(materials.materials_list) # Write materials to voices
score.RewriteMeter(materials.time_signatures)

score = score.score # access the abjad score inside muda score instatiation

segment_01 = abjad.LilyPondFile(items=[score])

file_name = os.path.basename(__file__)
file_name = os.path.splitext(file_name)[0]
score_dir = (
    "/Users/Davi/Composição/2021/"
    "a_rua_dos_cataventos/a_rua_dos_cataventos/score/"
)
ly_file_path = (score_dir + str(file_name) + ".ly")
abjad.persist.as_ly(segment_01, ly_file_path=ly_file_path)  # Lilypond

# Save LilyPond and PDF files to be illustrated (as brinca)
if __name__ == "__main__":
    score_block = abjad.Block(name="score")
    layout_block = abjad.Block(name="layout")
    midi_block = abjad.Block(name="midi")

    segment_00 = (
        r'\include "/Users/Davi/Composição/2021/a_rua_dos_cataventos/'
        'a_rua_dos_cataventos/segments/illustrations/illustration_segment_00.ly"'
    )
    include_container = abjad.Container()
    literal = abjad.LilyPondLiteral(segment_00, "opening")
    abjad.attach(literal, include_container)
    container = abjad.Container(
        [include_container, score],
        simultaneous=True,
    )

    score_block.items.append(container)
    score_block.items.append(layout_block)
    score_block.items.append(midi_block)

    includes = [
        "/Users/Davi/Composição/2021/a_rua_dos_cataventos/"
        "a_rua_dos_cataventos/segments/illustrations/illustration_stylesheet.ily"
    ]
    segment_01_illustration = abjad.LilyPondFile(items=[score_block], includes = includes)
    # print(abjad.lilypond(segment_01_illustration))

    new_file = (
        os.path.dirname(__file__) + "/illustrations/" + str(file_name)
    )

    abjad.persist.as_pdf(segment_01_illustration, pdf_file_path=(new_file + ".pdf"))  # PDF
    abjad.persist.as_ly(segment_01_illustration, ly_file_path=(new_file + ".ly"))  # PDF
    abjad.persist.as_midi(segment_01_illustration, midi_file_path=(new_file + ".midi"))  # PDF

    # opens pdf
    abjad.io.open_file((new_file + ".pdf"))
    # opens midi file
    os.system("timidity " + new_file + ".midi")


