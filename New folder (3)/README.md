# Python Audio Envelope Project

This project contains a Python script (`py.py`) for generating sound wave data with an ADSR envelope.

## What it includes

- `ADSREnvelope` class for attack, decay, sustain, and release shaping
- Wave generation structure for audio signal creation
- `scipy.io.wavfile` import for potential WAV file export

## Requirements

Install dependencies with:

```bash
pip install numpy scipy
```

## Run

From this folder, run:

```bash
python py.py
```

## Notes

- The current script appears to be a work in progress and may need fixes before successful execution.
- You can extend this project by adding waveform types and writing generated arrays to `.wav` files.
