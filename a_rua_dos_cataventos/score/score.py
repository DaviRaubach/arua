# -*- coding: utf-8 -*-

# Open virtual environment
# #!$HOME/github/my_venv/bin/python
# On Sublime Text use new build system and point to virtual environment
# Script file to finalize score


import os
# import shutil

from a_rua_dos_cataventos.segments import segment_01

import abjad

# Get the current working directory
cwd = os.getcwd()
# Change the current working directory
os.chdir(
    "/Users/Davi/Composição/2021/"
    "a_rua_dos_cataventos/a_rua_dos_cataventos/score"
)

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))

# Runs LilyPond to compile the score
os.system("lilypond " + "score.ly")

# Opens the PDF
abjad.io.open_file("score.pdf")

# Opens midi file
# os.system("timidity score.midi")


# # Paths
# srcdir = (
#     "/Users/Davi/Composição/2021/"
#     "a_rua_dos_cataventos/a_rua_dos_cataventos/segments"
# )
# dstdir = (
#     "/Users/Davi/Composição/2021/"
#     "a_rua_dos_cataventos/a_rua_dos_cataventos/score"
# )

# segments = [
#     segment_01.segment_01,
# ]
# segment_files = [
#     segment_01.segment_file,
# ]

# for segment, file in zip(segments, segment_files):
#     _file = os.path.splitext(file)[0]  # Path
#     segment_ly = str(str(_file) + ".ly")
#     abjad.persist.as_ly(segment, ly_file_path=segment_ly)  # Lilypond

# # Copies "segment_0X.ly" files to score folder
# for basename in os.listdir(srcdir):
#     if basename.endswith(".ly"):
#         pathname = os.path.join(srcdir, basename)
#         if os.path.isfile(pathname):
#             shutil.copy2(pathname, dstdir)
