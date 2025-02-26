import librosa
import pandas

class converter():
    def __init__(self,waveform, sampling_rate):
        self.waveform = waveform
        self.sampling_rate = sampling_rate

    def get_pandas(self):
        return pandas.DataFrame(self.waveform).transpose()

    def get_sampling_rate(self):
        return self.sampling_rate

class file_converter(converter):
    def __init__(self,file_path):
        self.filename = file_path
        super().__init__(*librosa.load(file_path))