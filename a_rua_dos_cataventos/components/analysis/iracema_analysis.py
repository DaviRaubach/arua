import muda
import abjad


# harmonics number should be equal to instruments notes sum (assign_to_instruments)
analysis = muda.IracemaAnalysis(
	    audioin="janela_cut.wav",
	    nharmonics = 6, 
	    denominator = 4
	    )

# analysis.pitch_range_filter("[C2, G7]")

container = analysis.abjad_container()

print(abjad.lilypond(container))

myd = analysis.assign_to_instruments(["Piano", "Violin"], [4, 1])
print(myd)



