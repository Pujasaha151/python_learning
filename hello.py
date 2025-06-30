pip install mne
from google.colab import files
files.upload()
import mne
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
raw = mne.io.read_raw_edf("S025R04.edf", preload=True)
print(raw.info)
raw.plot
channel = 'Cp5.'
srate = int(raw.info['sfreq'])
segment_samples = srate*5
channel_index = raw.ch_names.index(channel)

data = raw.get_data()

x = data[0, :segment_samples]

times = raw.times[:segment_samples]

plt.plot(times, x)
plt.title(f"Original EEG Segment from {channel}")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
N = len(x)
t = np.arange(N) / srate

X = np.zeros(N, dtype=complex)
for freq in range(N):
    csw = np.exp(-1j * 2 * np.pi * freq * t)
    X[freq] = np.sum(x * csw)

amps = 2 * np.abs(X) / N
freqs = np.linspace(0, srate, N)

plt.stem(freqs[:N//2], amps[:N//2])
plt.title("Amplitude Spectrum (5-second EEG segment)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.xlim(0, 50)
plt.show()
alpha_band = (8, 13)
beta_band = (13, 30)

alpha_idx = np.where((freqs >= alpha_band[0]) & (freqs <= alpha_band[1]))[0]
beta_idx = np.where((freqs >= beta_band[0]) & (freqs <= beta_band[1]))[0]

alpha_peaks, _ = find_peaks(amps[alpha_idx])
beta_peaks, _ = find_peaks(amps[beta_idx])

if len(alpha_peaks) > 0:
    alpha_peak_idx = alpha_idx[alpha_peaks[np.argmax(amps[alpha_idx][alpha_peaks])]]
    alpha_peak_freq = freqs[alpha_peak_idx]
    alpha_peak_amp = amps[alpha_peak_idx]
else:
    alpha_peak_freq, alpha_peak_amp = None, None

if len(beta_peaks) > 0:
    beta_peak_idx = beta_idx[beta_peaks[np.argmax(amps[beta_idx][beta_peaks])]]
    beta_peak_freq = freqs[beta_peak_idx]
    beta_peak_amp = amps[beta_peak_idx]
else:
    beta_peak_freq, beta_peak_amp = None, None

print(f"Dominant alpha frequency: {alpha_peak_freq:.2f} Hz with amplitude {alpha_peak_amp:.6f}")
print(f"Dominant beta frequency: {beta_peak_freq:.2f} Hz with amplitude {beta_peak_amp:.6f}")
plt.stem(freqs[:N//2], amps[:N//2])
plt.plot(alpha_peak_freq, alpha_peak_amp, 'ro', label=f'Alpha Peak ({alpha_peak_freq:.2f} Hz)')
plt.plot(beta_peak_freq, beta_peak_amp, 'go', label=f'Beta Peak ({beta_peak_freq:.2f} Hz)')
plt.xlim(0, 40)
plt.title("Amplitude Spectrum with Alpha and Beta Peaks")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()
N = len(X)

X_filtered = np.zeros_like(X, dtype=complex)

def find_freq_idx(freq_val):
    return np.argmin(np.abs(freqs - freq_val))

alpha_idx = find_freq_idx(alpha_peak_freq)
beta_idx = find_freq_idx(beta_peak_freq)

X_filtered[alpha_idx] = X[alpha_idx]
X_filtered[beta_idx] = X[beta_idx]

if alpha_idx != 0:
    X_filtered[N - alpha_idx] = X[N - alpha_idx]
if beta_idx != 0:
    X_filtered[N - beta_idx] = X[N - beta_idx]

# Compute Inverse DFT (IDFT)
reconstructed_signal = np.zeros(N)
for n in range(N):
    s = 0
    for k in range(N):
        s += X_filtered[k] * np.exp(1j * 2 * np.pi * k * n / N)
    reconstructed_signal[n] = s.real / N


plt.figure(figsize=(12,6))
plt.plot(t, x, label='Original Signal')
plt.plot(t, reconstructed_signal, label='Reconstructed Signal (Alpha + Beta)', linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.title('EEG Signal Reconstruction using Alpha and Beta Components')
plt.show()
