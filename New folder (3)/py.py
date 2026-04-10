import numpy as np
from scipy.io import wavfile
import warnings


class ADSREnvelope:
    def __init__(self, attack_time, decay_time, sustain_level, release_time):
        self.attack_time = attack_time
        self.decay_time = decay_time
        self.sustain_level = sustain_level
        self.release_time = release_time

    def get_envelope_array(self, gate_duration, sample_rate):
        # 1. Calculate base samples
        attack_samples = int(self.attack_time * sample_rate)
        decay_samples = int(self.decay_time * sample_rate)
        release_samples = int(self.release_time * sample_rate)
        gate_samples = int(gate_duration * sample_rate)

        sustain_samples = gate_samples - (attack_samples + decay_samples)

        if sustain_samples < 0:
            sustain_samples = 0

        attack_phase = np.linspace(0, 1, attack_samples)
        decay_phase = np.linspace(1, self.sustain_level, decay_samples)
        sustain_phase = np.full(sustain_samples, self.sustain_level)
        release_phase = np.linspace(self.sustain_level, 0, release_samples)

        envelope_array = np.concatenate([attack_phase, decay_phase, sustain_phase, release_phase])

        return envelope_array


class wavefrom:
    def __init__(self, frequency, amplitude=1, duration=None, sample_rate=44100, envelope=None):
        self.frequency = frequency
        self.amplitude = amplitude
        self.duration = duration
        self.sample_rate = sample_rate
        self.envelope = envelope

    def generate_waveform(self):
        if self.envelope:
            return self.duration + self.envelope.release_time
        return self.duration

    def apply_envelope(self, wave_array):
        if self.envelope:
            env_array = self.envelope.get_envelope_array(self.duration, self.sample_rate)
            return wave_array * env_array
        return wave_array


class SineWave(wavefrom):
    def generate(self):
        # We must query the parent class for the TRUE length of the array
        actual_duration = self.generate_waveform()
        total_samples = int(self.sample_rate * actual_duration)

        t = np.linspace(0, actual_duration, total_samples, endpoint=False)
        wave_array = self.amplitude * np.sin(2 * np.pi * self.frequency * t)

        return self.apply_envelope(wave_array)
