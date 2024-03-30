import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor
import librosa
import os


device = "cuda:0" if torch.cuda.is_available() else "cpu"
# torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
save_directory = "./models"
processor = AutoProcessor.from_pretrained(save_directory)
model = AutoModelForSpeechSeq2Seq.from_pretrained(save_directory)
forced_decoder_ids = processor.get_decoder_prompt_ids(language="zh", task="transcribe")
print(type(forced_decoder_ids))
print(forced_decoder_ids)
model.to(device)


data_path_dir = './data'
data_path = [os.path.join(data_path_dir, file) for file in os.listdir(data_path_dir)]

def load_audio(audio_path):
    waveform, sample_rate = librosa.load(audio_path, sr=16000)
    return waveform, sample_rate

for audio in data_path[0:5]:
    print(audio)
    waveform, sample_rate = load_audio(audio)
    print(f"the shape of waveform is {waveform.shape}")
    print("-------------------")
    input_features = processor(waveform, sampling_rate=sample_rate, return_tensors="pt").input_features.to(device)
    print('-------------------')
    
# generate token ids
    predicted_ids = model.generate(input_features, forced_decoder_ids=forced_decoder_ids)
    # print(f"the predicted_ids is {predicted_ids}")
# decode token ids to text
    transcription = processor.batch_decode(predicted_ids,skip_special_tokens=True)
    print(transcription)
