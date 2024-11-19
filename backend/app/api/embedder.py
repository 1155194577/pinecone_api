import librosa
import numpy as np 
class MusicEmbedder:
    def __init__(self, min_map, max_map):
        self.min_map = min_map
        self.max_map = max_map

    def min_max_scale(self, x, feature):
        """Scales the input value x using the min and max for the specified feature."""
        min_val = self.min_map.get(feature)
        max_val = self.max_map.get(feature)

        if min_val is None or max_val is None:
            raise ValueError(f"Min and Max values must be provided for feature '{feature}'.")

        # Prevent division by zero
        if max_val - min_val == 0:
            raise ValueError(f"Max value and min value are the same for feature '{feature}' during scaling.")
        
        return (x - min_val) / (max_val - min_val)

    def normalize(self, vector):
        """Normalizes the vector to have a magnitude of 1."""
        magnitude = np.linalg.norm(vector)
        if magnitude == 0:
            return vector  # Return original vector if it's zero
        return vector / magnitude

    def convert_music_to_vector(self, music):
        """Converts music features to a scaled and normalized vector."""
        # Extract and scale values from feature_map
        feature_map = music.feature_to_dict()
        vector = np.array([self.min_max_scale(value, feature) for feature, value in feature_map.items()])
        # Normalize the resulting vector to have a magnitude of 1
        return self.normalize(vector)

class Music:
    def __init__(self, y, sr, stability_score=None, beat_strength_score=None, tempo=None, dynamic_range=None, mean_rmse=None, mean_spectral_centroid=None,music_name=None,audio_url=None):
        self.y = y
        self.sr = sr
        self.onset_env = librosa.onset.onset_strength(y=self.y, sr=self.sr)
        self.stability_score = stability_score
        self.beat_strength_score = beat_strength_score
        self.tempo = tempo
        self.dynamic_range = dynamic_range
        self.mean_rmse = mean_rmse
        self.mean_spectral_centroid = mean_spectral_centroid
        self.music_name = music_name
        self.audio_url = audio_url

    def find_tempo(self):
        tempo, _ = librosa.beat.beat_track(y=self.y, sr=self.sr)
        return tempo[0]

    def find_stability_score(self):
        tempogram = librosa.feature.tempogram(onset_envelope=self.onset_env, sr=self.sr)
        grad_tempogram = np.gradient(tempogram, axis=1)
        avg_grad = np.mean(np.abs(grad_tempogram))
        return avg_grad

    def find_beat_strength_score(self):
        onset_frames = librosa.onset.onset_detect(onset_envelope=self.onset_env, sr=self.sr)
        onset_strengths = self.onset_env[onset_frames]
        avg_beat_strength = np.mean(onset_strengths)
        return avg_beat_strength

    def find_dynamic_range(self):
        rmse = librosa.feature.rms(y=self.y)[0]
        peak_amplitude = np.max(rmse)
        trough_amplitude = np.min(rmse)
        dynamic_range = peak_amplitude - trough_amplitude
        return dynamic_range

    def find_rms_amplitude(self):
        rmse = librosa.feature.rms(y=self.y)[0]
        mean_rmse = np.mean(rmse)
        return mean_rmse

    def find_mean_spectral_centroid(self):
        spectral_centroids = librosa.feature.spectral_centroid(y=self.y + 0.01, sr=self.sr)[0]
        mean_spectral_centroid = np.mean(spectral_centroids)
        return mean_spectral_centroid

    def compute_music_features(self):
        """Compute various music features and update class attributes."""

        # Compute each feature and store it in the respective attribute
        self.tempo = self.find_tempo()

        self.stability_score = self.find_stability_score()

        self.beat_strength_score = self.find_beat_strength_score()

        self.dynamic_range = self.find_dynamic_range()

        self.mean_rmse = self.find_rms_amplitude()

        self.mean_spectral_centroid = self.find_mean_spectral_centroid()

    def __str__(self):
        """String representation of the music features."""
        return (f"Tempo: {self.tempo}\n"
                f"Stability Score: {self.stability_score}\n"
                f"Beat Strength Score: {self.beat_strength_score}\n"
                f"Dynamic Range: {self.dynamic_range}\n"
                f"Mean RMS Amplitude: {self.mean_rmse}\n"
                f"Mean Spectral Centroid: {self.mean_spectral_centroid}")

    def feature_to_dict(self):
        """Return a dictionary representation of the music features."""
        return {
            "tempo": self.tempo,
            "stability_score": self.stability_score,
            "beat_strength_score": self.beat_strength_score,
            "dynamic_range": self.dynamic_range,
            "mean_rmse": self.mean_rmse,
            "mean_spectral_centroid": self.mean_spectral_centroid
        }

