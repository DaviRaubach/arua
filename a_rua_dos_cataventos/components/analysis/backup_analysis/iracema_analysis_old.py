import iracema
import matplotlib.pyplot as plt
import numpy as np
import abjad
import muda

def IracemaAnalysis(audioin, nharmonics, denominator):
	audio = iracema.Audio(audioin)

	# audio.play()
	# audio.plot()

	# specifying window and hop sizes
	window, hop = 2048, 1024

	# calculating the FFT
	fft = iracema.spectral.fft(audio, window, hop)

	# plotting the spectrogram
	# iracema.plot.plot_spectrogram(fft)

	# calculating the RMS
	# rms = iracema.features.rms(audio, window, hop)

	# plotting the RMS
	# rms.plot()

	# calculating the Peak Envelope
	# peak = iracema.features.peak_envelope(audio, window, hop)

	# plotting the Peak Envelope
	# peak.plot()

	# extract pitch
	hps_pitch = iracema.pitch.hps(fft, minf0=1, maxf0=1000)

	#extract harmonics
	harmonics = iracema.harmonics.extract(fft, hps_pitch, nharm=nharmonics)


	# plot the harmonics over the spectrogram
	# iracema.plot.plot_audio_spectrogram_harmonics(
	# 	audio=audio,
	# 	rms=rms,
	# 	peak_envelope=peak,
	# 	fft=fft,
	# 	fzero=harmonics['frequency'],
	# 	harmonics=harmonics['frequency'],
	# 	fftlim=(0,12000)
	# 	)

	# print(harmonics['frequency'].time)
	x = harmonics['frequency'].data
	y = harmonics['frequency'].time
	# print(x.shape, y.shape)
	# print(x[1].shape)
	# for n, data in enumerate(x):
	#     print(n)
	#     plt.plot(y, x[n])

	print("fs:", audio.fs)

	freq_list = []
	for n, data in enumerate(x):
	    if n != 0:
	        freq_sub_list = []
	        samples = data.shape[0]
	        measure = 44.1 * 4
	        half_second = int(44.1 / denominator)
	        mymod = int(samples / half_second)
	        for i, d in enumerate(data):
	            if i % mymod == 0:
	                freq_sub_list.append(d)
	        freq_list.append(freq_sub_list)


	freq_list = np.array(freq_list)
	print(freq_list[0, 2])
	print(freq_list.shape)

	all_pitches = []
	container = abjad.Container()
	for n in range(freq_list.shape[1]):
		pitches = []
		for i, list_ in enumerate(freq_list):
			pitches.append(abjad.NamedPitch.from_hertz(freq_list[i, n]))
		chord = abjad.Chord("<e' g' c''>4")
		chord.written_duration = abjad.Duration(1, denominator)
		chord.written_pitches = pitches
		container.append(chord)

	print(abjad.lilypond(container))
	voice = abjad.Voice()
	voice.append(container)
	abjad.show(voice)
	return container


analysis = IracemaAnalysis("janela_cut.wav", 12, 8)
# audio = iracema.Audio("janela_cut.wav")

# # audio.play()
# # audio.plot()

# # specifying window and hop sizes
# window, hop = 2048, 1024

# # calculating the FFT
# fft = iracema.spectral.fft(audio, window, hop)

# # plotting the spectrogram
# # iracema.plot.plot_spectrogram(fft)

# # calculating the RMS
# rms = iracema.features.rms(audio, window, hop)

# # plotting the RMS
# # rms.plot()

# # calculating the Peak Envelope
# peak = iracema.features.peak_envelope(audio, window, hop)

# # plotting the Peak Envelope
# # peak.plot()


# # extract pitch
# hps_pitch = iracema.pitch.hps(fft, minf0=1, maxf0=1000)

# #extract harmonics
# harmonics = iracema.harmonics.extract(fft, hps_pitch, nharm=12)


# # plot the harmonics over the spectrogram
# # iracema.plot.plot_audio_spectrogram_harmonics(
# # 	audio=audio,
# # 	rms=rms,
# # 	peak_envelope=peak,
# # 	fft=fft,
# # 	fzero=harmonics['frequency'],
# # 	harmonics=harmonics['frequency'],
# # 	fftlim=(0,12000)
# # 	)

# # print(harmonics['frequency'].time)
# x = harmonics['frequency'].data
# y = harmonics['frequency'].time
# print(x.shape, y.shape)
# print(x[1].shape)
# for n, data in enumerate(x):
#     print(n)
#     plt.plot(y, x[n])



# freq_list = []
# for n, data in enumerate(x):
#     if n != 0:
#         freq_sub_list = []
#         samples = data.shape[0]
#         half_second = int(0.5 * 44.1)
#         mymod = int(samples/half_second)
#         for i, d in enumerate(data):
#             if i % mymod == 0:
#                 freq_sub_list.append(d)
#         freq_list.append(freq_sub_list)


# freq_list = np.array(freq_list)
# print(freq_list[0, 2])
# print(freq_list.shape)

# all_pitches = []
# container = abjad.Container()
# for n in range(freq_list.shape[1]):
# 	pitches = []
# 	for i, list_ in enumerate(freq_list):
# 		pitches.append(abjad.NamedPitch.from_hertz(freq_list[i, n]))
# 	chord = abjad.Chord("<e' g' c''>4")
# 	chord.written_duration = abjad.Duration(1, 8)
# 	chord.written_pitches = pitches
# 	container.append(chord)

# print(abjad.lilypond(container))
# voice = abjad.Voice(container)
# abjad.show(voice)
