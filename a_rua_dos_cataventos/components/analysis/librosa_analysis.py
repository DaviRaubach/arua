import librosa
import librosa.display
import numpy as np
import sklearn.decomposition
import matplotlib.pyplot as plt


# Decompose a magnitude spectrogram into 32 components with NMF

y, sr = librosa.load(librosa.ex('choice'), duration=5)
S = np.abs(librosa.stft(y))
comps, acts = librosa.decompose.decompose(S, n_components=8)

# Sort components by ascending peak frequency

comps, acts = librosa.decompose.decompose(
    S, n_components=16, sort=True)

print(comps.shape)
# Or with sparse dictionary learning


T = sklearn.decomposition.MiniBatchDictionaryLearning(n_components=16)
scomps, sacts = librosa.decompose.decompose(S, transformer=T, sort=True)

print(scomps.shape)


fig, ax = plt.subplots(nrows=1, ncols=2)


librosa.display.specshow(
    librosa.amplitude_to_db(
        comps, ref=np.max
    ),
    y_axis='log', ax=ax[0]
)
ax[0].set(title='Components')
librosa.display.specshow(acts, x_axis='time', ax=ax[1])
ax[1].set(ylabel='Components', title='Activations')
fig, ax = plt.subplots(nrows=2, sharex=True, sharey=True)
librosa.display.specshow(
    librosa.amplitude_to_db(
        S, ref=np.max
    ),
    y_axis='log', 
    x_axis='time', 
    ax=ax[0]
)
ax[0].set(title='Input spectrogram')
ax[0].label_outer()
S_approx = comps.dot(acts)
img = librosa.display.specshow(
    librosa.amplitude_to_db(
        S_approx, ref=np.max
    ),
    y_axis='log', 
    x_axis='time', 
    ax=ax[1]
)
ax[1].set(title='Reconstructed spectrogram')
fig.colorbar(img, ax=ax, format="%+2.f dB")

plt.show()
