#!/usr/bin/env python3
"""Inspect a single audio file: basic properties, average spectrum, spectrogram.

This is the starting point of the analysis. It answers one question before any
comparison logic exists: can we load the audio and see its frequency content?

Usage:
    python src/inspect_audio.py data/audio/m01_mine.wav
"""

import sys
from pathlib import Path

import librosa
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

REPO = Path(__file__).resolve().parent.parent
FIGDIR = REPO / "results" / "figures"

# Analysis is capped below the codec rolloff of lossy reference material, so
# that a comparison never attributes a codec artifact to a mixing decision.
FMAX = 16000


def load(path):
    """Load as mono at the file's own sample rate.

    librosa resamples to 22050 Hz by default, which would throw away everything
    above 11 kHz. sr=None keeps the original rate. Mono because spectral balance
    is the question here; stereo width comes later.
    """
    y, sr = librosa.load(path, sr=None, mono=True)
    return y, sr


def describe(path, y, sr):
    info = sf.info(path)
    peak = float(np.max(np.abs(y)))
    rms = float(np.sqrt(np.mean(y ** 2)))

    print(f"file        {Path(path).name}")
    print(f"sample rate {sr} Hz")
    print(f"channels    {info.channels} (analyzed as mono)")
    print(f"duration    {len(y) / sr:.1f} s")
    print(f"peak        {20 * np.log10(peak):.1f} dBFS")
    print(f"rms         {20 * np.log10(rms):.1f} dBFS")
    print(f"centroid    {librosa.feature.spectral_centroid(y=y, sr=sr).mean():.0f} Hz")

    if peak >= 0.999:
        print("  ! peak at full scale - the file may be clipped")


def average_spectrum(y, sr, n_fft=8192):
    """Long-term average spectrum: the magnitude of each frequency bin,
    averaged over the whole file. Smooths past individual notes and shows
    the overall tonal balance, which is what mixing decisions act on.
    """
    S = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=n_fft // 4))
    mag = S.mean(axis=1)
    freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    db = librosa.amplitude_to_db(mag, ref=np.max)
    return freqs, db


def plot(path, y, sr):
    FIGDIR.mkdir(parents=True, exist_ok=True)
    stem = Path(path).stem

    freqs, db = average_spectrum(y, sr)
    keep = (freqs >= 20) & (freqs <= FMAX)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8))

    ax1.semilogx(freqs[keep], db[keep], linewidth=1)
    ax1.set_xlim(20, FMAX)
    ax1.set_ylim(-80, 5)
    ax1.set_xlabel("Frequency (Hz)")
    ax1.set_ylabel("Magnitude (dB, relative to peak)")
    ax1.set_title(f"Long-term average spectrum - {stem}")
    ax1.grid(True, which="both", alpha=0.3)
    # The region where buildup is usually described as muddiness.
    ax1.axvspan(200, 500, alpha=0.12, color="tab:orange")
    ax1.text(300, 0, "200-500 Hz", ha="center", fontsize=9, color="tab:orange")

    D = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft=2048)), ref=np.max)
    img = librosa.display.specshow(D, sr=sr, x_axis="time", y_axis="log", ax=ax2)
    ax2.set_ylim(20, FMAX)
    ax2.set_title("Spectrogram")
    fig.colorbar(img, ax=ax2, format="%+2.0f dB")

    fig.tight_layout()
    out = FIGDIR / f"{stem}_spectrum.png"
    fig.savefig(out, dpi=140)
    print(f"\nwrote {out.relative_to(REPO)}")


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python src/inspect_audio.py <audio file>")

    path = sys.argv[1]
    if not Path(path).is_file():
        sys.exit(f"not a file: {path}")

    y, sr = load(path)
    describe(path, y, sr)
    plot(path, y, sr)


if __name__ == "__main__":
    main()
